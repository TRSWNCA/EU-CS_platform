# Generated by Django 2.2.10 on 2020-04-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_delete_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='doingAtHome',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
