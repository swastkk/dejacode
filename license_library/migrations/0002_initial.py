# Generated by Django 4.2.7 on 2023-11-27 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("policy", "0001_initial"),
        ("license_library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="license",
            name="usage_policy",
            field=models.ForeignKey(
                blank=True,
                help_text="An administrator can communicate company policy for an entry by setting the Usage Policy indicator.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="policy.usagepolicy",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="licensetaggroupassignedtag",
            unique_together={
                ("dataspace", "uuid"),
                ("license_tag_group", "license_tag"),
            },
        ),
        migrations.AlterUniqueTogether(
            name="licensetaggroup",
            unique_together={("dataspace", "uuid"), ("dataspace", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="licensetag",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="licensestyle",
            unique_together={("dataspace", "uuid"), ("dataspace", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="licensestatus",
            unique_together={("dataspace", "uuid"), ("dataspace", "code")},
        ),
        migrations.AlterUniqueTogether(
            name="licenseprofileassignedtag",
            unique_together={("license_profile", "license_tag"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="licenseprofile",
            unique_together={("dataspace", "uuid"), ("dataspace", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="licensechoice",
            unique_together={("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="licensecategory",
            unique_together={("dataspace", "label"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="licenseassignedtag",
            unique_together={("license", "license_tag"), ("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="licenseannotation",
            unique_together={("dataspace", "uuid")},
        ),
        migrations.AlterUniqueTogether(
            name="license",
            unique_together={
                ("dataspace", "key"),
                ("dataspace", "short_name"),
                ("dataspace", "uuid"),
                ("dataspace", "name"),
            },
        ),
    ]
