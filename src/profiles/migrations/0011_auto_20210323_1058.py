# Generated by Django 2.2.13 on 2021-03-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210319_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='former_member',
            new_name='ecsa_former_member',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='invoice_id',
            new_name='ecsa_invoice_id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='member_since',
            new_name='ecsa_member_since',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='payment_revision',
            new_name='ecsa_payment_revision',
        ),
        migrations.AddField(
            model_name='profile',
            name='ecsa_requested_join',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]