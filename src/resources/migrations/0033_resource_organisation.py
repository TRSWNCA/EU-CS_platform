# Generated by Django 2.2.13 on 2020-08-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_auto_20200814_1238'),
        ('resources', '0032_auto_20200519_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='organisation',
            field=models.ManyToManyField(to='organisations.Organisation'),
        ),
    ]