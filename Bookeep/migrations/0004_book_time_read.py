# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 12:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bookeep', '0003_auto_20161126_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_read',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 26, 12, 12, 10, 697801, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
