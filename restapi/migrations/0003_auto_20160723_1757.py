# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20160723_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scan',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='scan',
            old_name='scan_ts',
            new_name='created',
        ),
    ]
