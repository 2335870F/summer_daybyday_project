# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-04 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0011_remove_extrainformation_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='photo',
            field=models.ImageField(default='cat_pics/default1.svg', upload_to='reminder_pics'),
        ),
    ]