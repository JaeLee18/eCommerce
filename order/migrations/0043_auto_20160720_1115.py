# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 11:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0042_auto_20160720_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 11, 15, 39, 2339), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='thisid',
            field=models.CharField(default='WPZPKPR3RTOWKUDN', max_length=16, null=True),
        ),
    ]
