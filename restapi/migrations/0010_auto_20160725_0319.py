# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 03:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20160725_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_status',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='upc',
            name='api_last_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='brand_id',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='brand_name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='calcium_dv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='calories_from_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='cholesterol',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='data_source',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='dietary_fiber',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='ingredients',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='iron_dv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='item_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='item_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='item_name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='saturated_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='serving_per_cont',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='serving_size_qty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='serving_size_unit',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='sodium',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='sugars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='total_carb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='total_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='vitamin_a_dv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upc',
            name='vitamin_c_dv',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
