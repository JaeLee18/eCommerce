# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 11:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0067_auto_20160720_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 11, 49, 51, 951928), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='uni_id',
            field=models.CharField(default='M9XD6NGPIAB35NEO', max_length=16, null=True),
        ),
    ]
