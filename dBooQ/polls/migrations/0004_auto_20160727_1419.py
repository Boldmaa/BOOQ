# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160727_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='firstPublishedYear',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishedYear',
            field=models.IntegerField(blank=True),
        ),
    ]
