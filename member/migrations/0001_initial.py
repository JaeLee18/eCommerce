# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-14 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('apply', '0002_auto_20160714_1808'),
        ('product', '__first__'),
        ('date', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRegistered', models.CharField(choices=[('0', '비회원'), ('1', '회원'), ('2', 'NAVER'), ('3', 'KAKAO')], max_length=1, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Member_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=128, null=True)),
                ('address1', models.CharField(blank=True, max_length=128, null=True)),
                ('address2', models.CharField(blank=True, max_length=128, null=True)),
                ('address3', models.CharField(blank=True, max_length=128, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Member_calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('1', '사유들')], max_length=100, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('modified', models.ManyToManyField(blank=True, null=True, to='date.Not_availble_date')),
                ('original', models.ManyToManyField(blank=True, null=True, to='date.Availble_date')),
            ],
        ),
        migrations.CreateModel(
            name='Member_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('product', models.ManyToManyField(blank=True, null=True, to='product.Product')),
                ('program', models.ManyToManyField(blank=True, null=True, to='product.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Member_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_etc', models.TextField(blank=True, null=True)),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apply.Coupon')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Member_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
    ]
