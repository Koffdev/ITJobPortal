# Generated by Django 4.1.3 on 2022-12-08 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_userrequest_options_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
