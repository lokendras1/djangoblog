# Generated by Django 2.1.5 on 2019-03-01 17:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190301_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 17, 31, 34, 189999, tzinfo=utc)),
        ),
    ]