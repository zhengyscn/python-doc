# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-08 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190607_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('男', 'Freshman'), ('女', 'Sophomore')], default='', max_length=1, verbose_name='性别'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(db_index=True, max_length=32, unique=True, verbose_name='用户名'),
        ),
    ]