# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190608_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=6, verbose_name='性别'),
        ),
    ]
