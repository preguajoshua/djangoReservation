# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20171012_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='persons',
            new_name='quantity',
        ),
    ]
