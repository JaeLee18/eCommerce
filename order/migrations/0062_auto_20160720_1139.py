# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 11:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0061_auto_20160720_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 11, 39, 27, 630545), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='uni_id',
            field=models.CharField(default='PXCO4RH0DIC8CMPZ', max_length=16, null=True),
        ),
    ]
