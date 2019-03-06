# Generated by Django 2.1.5 on 2019-02-13 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190213_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 13, 13, 56, 28, 599318, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]