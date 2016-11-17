# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20160720_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='uid',
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 10, 43, 7, 589710), null=True),
        ),
    ]
