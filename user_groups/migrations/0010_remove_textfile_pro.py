# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_groups', '0009_auto_20170930_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textfile',
            name='pro',
        ),
    ]