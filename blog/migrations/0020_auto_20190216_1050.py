# Generated by Django 2.1.5 on 2019-02-16 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190216_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 10, 50, 34, 800094, tzinfo=utc)),
        ),
    ]
