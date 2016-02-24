from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cluster(models.Model):
    name = models.CharField(blank=False, max_length=50)


class Scores(models.Model):
    points = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey('Event', related_name='scores')
    cluster = models.ForeignKey(Cluster, related_name='scores')


class Event(models.Model):
    cluster = models.ManyToManyField(Cluster, through=Scores)
    name = models.CharField(blank=False, max_length=50, unique=True)
    is_major = models.BooleanField(default=True)
    start_time = models.DateTimeField(blank=False, null=False)

