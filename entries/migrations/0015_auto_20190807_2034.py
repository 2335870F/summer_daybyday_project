# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-07 20:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0014_entry_date_last_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='supercat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='entries.Category'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extrainformation',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entries.Entry'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entries.Entry'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
