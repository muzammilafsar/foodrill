# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20170110_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item_description',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item_name',
        ),
    ]
