# Generated by Django 2.2.13 on 2021-05-21 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecsa', '0003_delegate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
