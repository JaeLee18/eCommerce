# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0071_auto_20160720_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 12, 8, 27, 468630), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='uni_id',
            field=models.CharField(default='X7PPOF2DB7RYZZK5', max_length=16, null=True),
        ),
    ]