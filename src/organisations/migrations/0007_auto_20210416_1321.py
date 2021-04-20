# Generated by Django 2.2.13 on 2021-04-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0006_auto_20210311_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_billing_city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_billing_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_billing_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_billing_postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_billing_street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Street'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_old_organisation_fee',
            field=models.BooleanField(default=False, verbose_name='Old organisation fee'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ecsa_reduced_fee',
            field=models.BooleanField(default=False, verbose_name='Reduced fee'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Street'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='vat_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
