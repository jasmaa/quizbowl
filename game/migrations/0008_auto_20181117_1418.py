# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-17 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20181115_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('Everything', 'Everything'), ('Science', 'Science'), ('History', 'History'), ('Literature', 'Literature')], default='Everything', max_length=30),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_end_time',
            field=models.FloatField(default=1542482301.137),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_start_time',
            field=models.FloatField(default=1542482300.137),
        ),
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.FloatField(default=1542482301.137),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_time',
            field=models.FloatField(default=1542482300.137),
        ),
    ]