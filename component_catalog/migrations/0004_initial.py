# Generated by Django 4.2.7 on 2023-11-27 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dje.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("policy", "0001_initial"),
        ("license_library", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("component_catalog", "0003_initial"),
        ("dje", "0001_initial"),
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcomponent",
            name="usage_policy",
            field=models.ForeignKey(
                blank=True,
                help_text="An administrator can communicate company policy for an entry by setting the Usage Policy indicator.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="policy.usagepolicy",
            ),
        ),
        migrations.AddField(
            model_name="packageassignedlicense",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="packageassignedlicense",
            name="license",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="packageassignedlicense",
            name="package",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="component_catalog.package",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="created_by",
            field=models.ForeignKey(
                editable=False,
                help_text="The application user who created the object.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_%(class)ss",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="last_modified_by",
            field=dje.fields.LastModifiedByField(
                editable=False,
                help_text="The application user who last modified the object.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modified_%(class)ss",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="licenses",
            field=models.ManyToManyField(
                through="component_catalog.PackageAssignedLicense",
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="usage_policy",
            field=models.ForeignKey(
                blank=True,
                help_text="An administrator can communicate company policy for an entry by setting the Usage Policy indicator.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="policy.usagepolicy",
            ),
        ),
        migrations.AddField(
            model_name="componenttype",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="componentstatus",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="componentkeyword",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedpackage",
            name="component",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="component_catalog.component",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedpackage",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedpackage",
            name="package",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="component_catalog.package",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedlicense",
            name="component",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="component_catalog.component",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedlicense",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="componentassignedlicense",
            name="license",
            field=models.ForeignKey(
                help_text="Select from list of licenses.",
                on_delete=django.db.models.deletion.PROTECT,
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="children",
            field=models.ManyToManyField(
                through="component_catalog.Subcomponent",
                to="component_catalog.component",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="configuration_status",
            field=models.ForeignKey(
                blank=True,
                help_text="The configuration status can be used to communicate the current stage of the review process and whether additional review is required.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="component_catalog.componentstatus",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="created_by",
            field=models.ForeignKey(
                editable=False,
                help_text="The application user who created the object.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_%(class)ss",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="last_modified_by",
            field=dje.fields.LastModifiedByField(
                editable=False,
                help_text="The application user who last modified the object.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modified_%(class)ss",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="licenses",
            field=models.ManyToManyField(
                help_text='The license that applies to a component. There could be more than one license, in which case a choice is usually required. The expression "(default)" next to the license name indicates that this license applies to the component even if you do not assert a particular license.',
                through="component_catalog.ComponentAssignedLicense",
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Owner is an optional field selected by the user to identify the original creator (copyright holder) of the  component. If this component is in its original, unmodified state, the component owner is associated with the original author/publisher. If this component has been copied and modified, the component  owner should be the owner that has copied and modified it.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="organization.owner",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="packages",
            field=models.ManyToManyField(
                through="component_catalog.ComponentAssignedPackage",
                to="component_catalog.package",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="type",
            field=models.ForeignKey(
                blank=True,
                help_text="A component type provides a label to filter and sort components.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="component_catalog.componenttype",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="usage_policy",
            field=models.ForeignKey(
                blank=True,
                help_text="An administrator can communicate company policy for an entry by setting the Usage Policy indicator.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="policy.usagepolicy",
            ),
        ),
        migrations.AddField(
            model_name="acceptablelinkage",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="subcomponentassignedlicense",
            unique_together={("subcomponent", "license"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="subcomponent",
            unique_together={("parent", "child"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="packageassignedlicense",
            unique_together={("package", "license"), ("dataspace", "uuid")},
        ),
        migrations.AddIndex(
            model_name="package",
            index=models.Index(fields=["md5"], name="component_c_md5_33e2c1_idx"),
        ),
        migrations.AddIndex(
            model_name="package",
            index=models.Index(fields=["sha1"], name="component_c_sha1_5b9041_idx"),
        ),
        migrations.AddIndex(
            model_name="package",
            index=models.Index(fields=["sha256"], name="component_c_sha256_dba399_idx"),
        ),
        migrations.AddIndex(
            model_name="package",
            index=models.Index(fields=["sha512"], name="component_c_sha512_a0eb10_idx"),
        ),
        migrations.AlterUniqueTogether(
            name="package",
            unique_together={
                ("dataspace", "uuid"),
                (
                    "dataspace",
                    "type",
                    "namespace",
                    "name",
                    "version",
                    "qualifiers",
                    "subpath",
                    "download_url",
                    "filename",
                ),
            },
        ),
        migrations.AlterUniqueTogether(
            name="componenttype",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="componentstatus",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="componentkeyword",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="componentassignedpackage",
            unique_together={("component", "package"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="componentassignedlicense",
            unique_together={("component", "license"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="component",
            unique_together={("dataspace", "name", "version"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="acceptablelinkage",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
    ]
