# Generated by Django 2.1.7 on 2019-03-04 08:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190303_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 8, 25, 46, 404018, tzinfo=utc)),
        ),
    ]
