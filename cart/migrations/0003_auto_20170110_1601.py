# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='price',
            new_name='item_price',
        ),
        migrations.AddField(
            model_name='cart',
            name='item_description',
            field=models.TextField(default='this is the description', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='item_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
