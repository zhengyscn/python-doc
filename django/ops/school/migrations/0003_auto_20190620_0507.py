# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-20 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190620_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Teacher', verbose_name='课程讲师'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='school.Course', verbose_name='别名'),
        ),
        migrations.AddField(
            model_name='teacherassistant',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Teacher', verbose_name='讲师'),
        ),
    ]
