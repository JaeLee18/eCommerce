# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0079_auto_20160720_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 21, 16, 46, 19, 280479), null=True),
        ),
    ]
