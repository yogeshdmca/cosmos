# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20170120_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='flat_number',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='flates', to='profile.FlatNumber'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.UserProfile'),
        ),
    ]
