# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
            ],
        ),
    ]
