# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160727_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='firstPublishedYear',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishedYear',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]