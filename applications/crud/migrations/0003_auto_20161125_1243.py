# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20161125_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='characteristic',
        ),
        migrations.AddField(
            model_name='cars',
            name='description',
            field=models.TextField(default='', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(default='test', upload_to='images/cars', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
            preserve_default=False,
        ),
    ]
