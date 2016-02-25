from __future__ import unicode_literals

from django.db import models


class Cluster(models.Model):
    name = models.CharField(max_length=15, primary_key=True,
                            help_text='The name of the cluster.')
    participated_events = models.ManyToManyField('Event', through='Score',
                                                 related_name='clusters')

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30, primary_key=True,
                            help_text='The name of the event.')
    location = models.CharField(max_length=30,
                                help_text='The location of the event.')
    begin_time = models.DateTimeField(
        help_text='The begin time and date of the event.')
    is_major = models.BooleanField(
        help_text='A boolean to represent whether this '
                  'event is a major event.')
    is_done = models.BooleanField(
        help_text='A boolean to represent whether this event is done.')

    def __unicode__(self):
        return self.name


class Score(models.Model):
    points = models.SmallIntegerField(
        default=0, help_text='The points earned.')
    cluster = models.ForeignKey('Cluster', related_name='scores',
                                help_text='The cluster this score belongs to.')
    event = models.ForeignKey(
        'Event', help_text='The event this score comes from.')

    def __unicode__(self):
        return '{0} points - {1} - {2}'.format(
            self.points, self.event, self.cluster)
