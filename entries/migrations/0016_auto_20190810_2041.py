# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-10 20:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0015_auto_20190807_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extrainformation',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Entry'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Entry'),
        ),
    ]
