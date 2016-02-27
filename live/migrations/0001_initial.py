# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('name', models.CharField(help_text='The name of this cluster.', max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(help_text='The name of this event.', max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(help_text='The location where this event is held.', max_length=50)),
                ('is_major', models.BooleanField(default=True, help_text='A boolean to determine this event is a major event.')),
                ('start_time', models.DateTimeField(help_text='The start time of this event.')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(help_text='A boolean to denote this match is over.')),
                ('event', models.ForeignKey(help_text='The event this match belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='live.Event')),
                ('left', models.ForeignKey(help_text='The left competitor.', on_delete=django.db.models.deletion.CASCADE, related_name='left_matches', to='live.Cluster')),
                ('loser', models.ForeignKey(blank=True, help_text='The loser of this match.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to='live.Cluster')),
                ('right', models.ForeignKey(help_text='The right competitor.', on_delete=django.db.models.deletion.CASCADE, related_name='right_matches', to='live.Cluster')),
                ('winner', models.ForeignKey(blank=True, help_text='The winner of this match.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='live.Cluster')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.SmallIntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], help_text='The rank for this cluster-event pair.')),
                ('cluster', models.ForeignKey(help_text='The cluster this rank belongs to.', on_delete=django.db.models.deletion.CASCADE, to='live.Cluster')),
                ('event', models.ForeignKey(help_text='The event this rank belongs to.', on_delete=django.db.models.deletion.CASCADE, to='live.Event')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rank',
            unique_together=set([('event', 'rank'), ('cluster', 'event')]),
        ),
    ]
