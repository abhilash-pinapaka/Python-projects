# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=15)),
                ('album_name', models.CharField(max_length=15)),
                ('album_logo', models.ImageField(upload_to=b'')),
                ('release_date', models.DateField(verbose_name='DD/MM/YYYY')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('singer', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=15)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
