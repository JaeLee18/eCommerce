# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20160721_1646'),
        ('order', '0096_auto_20160725_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member_cart'),
        ),
    ]
