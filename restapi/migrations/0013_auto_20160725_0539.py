# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0012_auto_20160725_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_status',
            field=models.TextField(default='Unknown', max_length=200),
        ),
    ]
