# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0080_auto_20160721_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 21, 16, 54, 24, 716517), null=True),
        ),
    ]