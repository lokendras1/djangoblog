# Generated by Django 2.1.5 on 2019-02-14 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190214_1907'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostModel',
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 19, 12, 26, 177731, tzinfo=utc)),
        ),
    ]
