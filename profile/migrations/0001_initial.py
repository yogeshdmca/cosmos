# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Job Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaving_type', models.CharField(choices=[('own', 'Home owner'), ('faimily', 'My Faimily member'), ('rent', 'rented'), ('pg', 'I am Leaving here paying guest')], max_length=40)),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('permanent_address', models.CharField(max_length=2000, verbose_name='Permanent address')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('doa', models.DateField(verbose_name='Date of Anniversary')),
                ('flat_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='profile.FlatNumber')),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='profile.JobCategory')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chields', to='profile.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInfomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=30)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='profile.FlatNumber')),
            ],
        ),
    ]
