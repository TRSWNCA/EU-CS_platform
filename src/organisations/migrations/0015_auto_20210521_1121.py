# Generated by Django 2.2.13 on 2021-05-21 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecsa', '0003_delegate'),
        ('organisations', '0014_auto_20210514_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='delegate1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delegate1', to='ecsa.Delegate'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='delegate2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delegate2', to='ecsa.Delegate'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='mainDelegate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_delegate', to='ecsa.Delegate'),
        ),
    ]
