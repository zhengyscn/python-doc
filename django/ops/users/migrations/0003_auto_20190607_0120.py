# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-07 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190607_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['update_time'], 'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
    ]
