# Generated by Django 2.2.13 on 2021-08-01 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='digest',
            name='nProjects',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='digest',
            name='nResources',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='digest',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='digest',
            name='slug',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]
