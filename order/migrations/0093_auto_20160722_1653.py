# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 16:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0092_auto_20160722_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 22, 16, 53, 44, 876868), null=True),
        ),
    ]