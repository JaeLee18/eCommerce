# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20160719_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 19, 15, 8, 31, 998834), null=True),
        ),
    ]