# Generated by Django 2.2.13 on 2021-05-21 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecsa', '0004_auto_20210521_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='userID',
            new_name='user',
        ),
    ]
