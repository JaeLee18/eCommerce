# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 11:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_auto_20160720_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 11, 27, 20, 653265), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='T2DUCUMXLDU4FWSQ', max_length=16, null=True),
        ),
    ]
