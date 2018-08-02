# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    class Meta:
        pass

    artist = models.CharField(max_length=15)
    album_name = models.CharField(max_length=15)
    album_logo = models.ImageField()
    release_date = models.DateField("DD/MM/YYYY")


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    singer = models.CharField(max_length= 100)
    genre = models.CharField(max_length=15)