# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-02-09 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0007_auto_20190208_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(choices=[('l', 'Liked'), ('d', 'Disliked'), ('u', 'Undecided')], max_length=1),
        ),
    ]
