# Generated by Django 4.1 on 2022-08-19 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_rename_date_watched_user_date_added'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ads',
            new_name='Ad',
        ),
    ]
