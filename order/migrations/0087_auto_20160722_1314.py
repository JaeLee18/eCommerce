# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0086_auto_20160721_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 22, 13, 14, 39, 330525), null=True),
        ),
    ]
