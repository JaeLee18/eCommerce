# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 16:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20160719_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_status',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order_status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 19, 16, 57, 45, 950060), null=True),
        ),
    ]