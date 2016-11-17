# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20160714_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping_info',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Shipping_info'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 19, 13, 26, 43, 789903), null=True),
        ),
    ]
