# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 17:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0077_auto_20160720_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 17, 26, 54, 696203), null=True),
        ),
    ]
