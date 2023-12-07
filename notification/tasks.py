#
# Copyright (c) nexB Inc. and others. All rights reserved.
# DejaCode is a trademark of nexB Inc.
# SPDX-License-Identifier: AGPL-3.0-only
# See https://github.com/nexB/dejacode for support or download.
# See https://aboutcode.org for more information about AboutCode FOSS projects.
#

import json
import logging

import requests
from celery.task import Task
from rest_framework.utils import encoders

logger = logging.getLogger("dje")


class DeliverHook(Task):
    max_retries = 2

    def run(self, target, payload, instance_id=None, hook_id=None, extra_headers=None, **kwargs):
        """
        target: the url to receive the payload
        payload: a python primitive data structure
        instance_id: a possibly None "trigger" instance ID
        hook_id: the ID of defining Hook object
        extra_headers: Additional headers such as Authentication ones
        """
        session = requests.Session()

        session.headers.update({"Content-Type": "application/json"})
        if extra_headers:
            session.headers.update(extra_headers)

        logger.info(f"Delivering Webhook hook_id={hook_id} to target={target}")
        try:
            session.post(url=target, data=payload)
        except requests.ConnectionError:
            delay_in_seconds = 2**self.request.retries
            self.retry(countdown=delay_in_seconds)


def deliver_hook_wrapper(target, payload, instance, hook):
    if hook.extra_payload:
        payload.update(hook.extra_payload)

    # Using ID's instead of objects for proper serialization
    kwargs = {
        "target": target,
        "payload": json.dumps(payload, cls=encoders.JSONEncoder),
        "hook_id": hook.id,
    }

    if instance:
        kwargs["instance_id"] = instance.id
    if hook.extra_headers:
        kwargs["extra_headers"] = hook.get_extra_headers()

    DeliverHook().apply_async(kwargs=kwargs)
