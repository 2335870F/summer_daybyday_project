# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-14 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0008_auto_20190711_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('photo', models.ImageField(default='cat_pics/default1.png', upload_to='reminder_pics')),
                ('importance', models.IntegerField(default=0)),
                ('date_last_edited', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(default='No content yet!')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
