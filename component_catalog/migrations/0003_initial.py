# Generated by Django 4.2.7 on 2023-11-27 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dje.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("component_catalog", "0002_initial"),
        ("dje", "0001_initial"),
        ("license_library", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="subcomponentassignedlicense",
            name="license",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="subcomponentassignedlicense",
            name="subcomponent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="component_catalog.subcomponent",
            ),
        ),
        migrations.AddField(
            model_name="subcomponent",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_parents",
                to="component_catalog.component",
            ),
        ),
        migrations.AddField(
            model_name="subcomponent",
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
            model_name="subcomponent",
            name="dataspace",
            field=models.ForeignKey(
                editable=False,
                help_text="A Dataspace is an independent, exclusive set of DejaCode data, which can be either nexB master reference data or installation-specific data.",
                on_delete=django.db.models.deletion.PROTECT,
                to="dje.dataspace",
            ),
        ),
        migrations.AddField(
            model_name="subcomponent",
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
            model_name="subcomponent",
            name="licenses",
            field=models.ManyToManyField(
                through="component_catalog.SubcomponentAssignedLicense",
                to="license_library.license",
            ),
        ),
        migrations.AddField(
            model_name="subcomponent",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_children",
                to="component_catalog.component",
            ),
        ),
    ]