# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-06-09 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0003_auto_20190617_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=256, verbose_name='Subject'),
        ),
    ]
