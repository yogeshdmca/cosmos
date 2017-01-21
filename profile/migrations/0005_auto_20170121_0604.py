# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20170121_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='flat_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flates', to='profile.FlatNumber'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.UserProfile'),
        ),
    ]
