# Generated by Django 4.2.6 on 2023-11-18 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appealing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 8, 44, 28, 206638, tzinfo=datetime.timezone.utc)),
        ),
    ]
