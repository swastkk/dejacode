# Generated by Django 4.2.7 on 2023-11-27 21:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AssociatedPolicy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, verbose_name="UUID"
                    ),
                ),
            ],
            options={
                "ordering": ["from_policy", "to_policy"],
            },
        ),
        migrations.CreateModel(
            name="UsagePolicy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, verbose_name="UUID"
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        help_text="You can choose an icon to associate with the usage policy from the available icons at https://fontawesome.com/icons?d=gallery&m=free",
                        max_length=50,
                    ),
                ),
                (
                    "color_code",
                    models.CharField(
                        blank=True,
                        help_text="You can specify a valid HTML color code (e.g. #FFFFFF) to apply to your icon.",
                        max_length=7,
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        help_text="Label is the text that you want to present to application users to describe a specific Usage Policy as it applies to an application object.",
                        max_length=50,
                    ),
                ),
                (
                    "guidelines",
                    models.TextField(
                        blank=True,
                        help_text="Guidelines explain the organization definition of a usage policy (approval level) and can also provide detailed requirements for compliance.",
                    ),
                ),
                (
                    "compliance_alert",
                    models.CharField(
                        blank=True,
                        choices=[("warning", "Warning"), ("error", "Error")],
                        help_text='Indicates how the usage of a DejaCode object (license, component, package, etc.) complies with organizational policy. Value choices include "Pass" (or empty, the default value), "Warning" (should be reviewed), and "Error" (fails compliance policy guidelines).',
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "usage policies",
                "ordering": ["content_type", "label"],
            },
        ),
    ]
