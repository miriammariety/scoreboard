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
    NONE = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    PLACES = (
        (NONE, 'None'),
        (FIRST, '1st Place'),
        (SECOND, '2nd Place'),
        (THIRD, '3rd Place'),
        (FOURTH, '4th Place')
    )
    points = models.SmallIntegerField(
        default=0, help_text='The points earned.')
    cluster = models.ForeignKey('Cluster', related_name='scores',
                                help_text='The cluster this score belongs to.')
    event = models.ForeignKey(
        'Event', help_text='The event this score comes from.')
    place = models.SmallIntegerField(
        choices=PLACES, default=NONE,
        help_text='The cluster\'s placement in this event.')

    class Meta:
        unique_together = (('event', 'place'), ('event', 'cluster'))

    def __unicode__(self):
        return '{0} points - {1} - {2}'.format(
            self.points, self.event, self.cluster)

    def calculate_score(self):
        place = self.place
        is_major = self.event.is_major
        if is_major:
            scores = [0, 30, 25, 20, 15]
        else:
            scores = [0, 15, 12, 9, 6]
        self.points = scores[place]
