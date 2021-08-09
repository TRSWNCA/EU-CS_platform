# Generated by Django 2.2.13 on 2021-08-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_submittedisvisible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='isVisible',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='submittedisVisible',
        ),
        migrations.AddField(
            model_name='profile',
            name='contentVisible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profileVisible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='digest',
            field=models.BooleanField(default=True),
        ),
    ]