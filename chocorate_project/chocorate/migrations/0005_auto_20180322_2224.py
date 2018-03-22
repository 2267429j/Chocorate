# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-22 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0004_auto_20180322_2211'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='chocolate',
            name='chocolate_type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='picture',
            field=models.ImageField(blank=True, help_text='Upload image of chocolate here', null=True, upload_to=''),
        ),
    ]
