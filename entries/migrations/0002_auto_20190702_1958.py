# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-02 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='bio',
            field=models.TextField(blank=True, default='Hello! I enjoy the opportunity to upload entries, create reminders, and plan ahead on this website!'),
        ),
    ]