# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20170121_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.UserInfo'),
        ),
    ]
