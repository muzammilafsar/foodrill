# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price_lrg',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price_md',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price_sml',
            field=models.FloatField(default=0.0),
        ),
    ]