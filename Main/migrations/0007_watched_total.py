# Generated by Django 4.1 on 2022-08-22 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_remove_user_account_number_remove_user_bank_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watched_Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_ads_watched', models.CharField(max_length=30)),
                ('date_watched', models.DateTimeField(default=django.utils.timezone.now)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_watched',),
            },
        ),
    ]
