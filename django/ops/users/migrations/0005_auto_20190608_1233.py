# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-08 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190608_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], max_length=1, verbose_name='性别'),
        ),
    ]
