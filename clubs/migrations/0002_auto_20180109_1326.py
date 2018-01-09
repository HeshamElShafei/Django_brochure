# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-09 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubsignup',
            name='membership',
            field=models.CharField(default='HomeClubMembership', max_length=250),
        ),
        migrations.AddField(
            model_name='clubsignup',
            name='option',
            field=models.CharField(default='Monthly', max_length=250),
        ),
    ]
