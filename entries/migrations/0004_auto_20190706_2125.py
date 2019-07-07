# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-06 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20190707_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_posted',
            new_name='date_last_edited',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='cook_time',
            new_name='importance',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='ingredients',
            new_name='key_info',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='steps',
            new_name='to_do',
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('CAT', 'Category'), ('CUS', 'All_courses'), ('SPE', 'Special Occasions')], max_length=25),
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='about',
            new_name='content',
        ),
    ]
