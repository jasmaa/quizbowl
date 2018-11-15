# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-15 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20181114_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='duration',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_time',
            field=models.FloatField(),
        ),
    ]