# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20160719_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 19, 17, 32, 28, 855847), null=True),
        ),
    ]
