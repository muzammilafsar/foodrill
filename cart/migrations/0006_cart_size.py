# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20170110_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
