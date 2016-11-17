# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 16:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0090_auto_20160722_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 22, 16, 53, 9, 14236), null=True),
        ),
        migrations.AlterField(
            model_name='shipping_info',
            name='duration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Shipping_duration'),
        ),
    ]