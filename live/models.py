from __future__ import unicode_literals

from django.db import models


class Cluster(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(
        max_length=30, help_text='The name of this cluster.')
    team_name = models.CharField(max_length=30, help_text='The team name.')
    image = models.ImageField(
        upload_to='cluster_image', help_text='The image for this cluster.',
        null=True, blank=True)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(
        max_length=30, help_text='The name of this event.')
    location = models.CharField(
        max_length=50, help_text='The location where this event is held.')
    is_major = models.BooleanField(
        default=True,
        help_text='A boolean to determine this event is a major event.')
    start_time = models.DateTimeField(
        help_text='The start time of this event.')

    def __unicode__(self):
        return self.name


class Match(models.Model):
    event = models.ForeignKey(
        'Event', related_name='matches',
        help_text='The event this match belongs to.')
    left = models.ForeignKey(
        'Cluster', related_name='left_matches',
        help_text='The left competitor.')
    right = models.ForeignKey(
        'Cluster', related_name='right_matches',
        help_text='The right competitor.')
    winner = models.ForeignKey(
        'Cluster', related_name='won_matches', null=True, blank=True,
        help_text='The winner of this match.')
    loser = models.ForeignKey(
        'Cluster', related_name='lost_matches', null=True, blank=True,
        help_text='The loser of this match.')
    start_time = models.DateTimeField(
        help_text='The start time of this match.')

    class Meta:
        verbose_name_plural = 'matches'

    def __unicode__(self):
        return '{left} vs. {right} - {event}'.format(
            left=self.left, right=self.right, event=self.event)


class Rank(models.Model):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    RANKS = (
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Third'),
        (FOURTH, 'Fourth')
    )
    cluster = models.ForeignKey(
        'Cluster', related_name='rankings',
        help_text='The cluster this rank belongs to.')
    event = models.ForeignKey(
        'Event', related_name='rankings',
        help_text='The event this rank belongs to.')
    rank = models.SmallIntegerField(
        choices=RANKS, help_text='The rank for this cluster-event pair.',
        default=0, blank=True)

    class Meta:
        unique_together = (('cluster', 'event'), ('event', 'rank'))

    @property
    def points(self):
        if self.event.is_major:
            points = [0, 30, 25, 20, 15]
        else:
            points = [0, 15, 12, 9, 6]
        return points[self.rank]

    def __unicode__(self):
        return 'Rank {rank} - {cluster} - {event}'.format(
            rank=self.rank, cluster=self.cluster, event=self.event)
