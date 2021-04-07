from uuid import uuid4
from os import path

from django.db import models

from speakers.models import Speaker
from schedules.models import Event


class Stream(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='streams')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='streams')
    live_url = models.URLField(blank=True, null=True)
    live_mixlr_audio = models.BooleanField(default=False)
    live = models.BooleanField(default=False)
    audio_views = models.IntegerField(default=0)
    video_views = models.IntegerField(default=0)

    class Meta:
        ordering = ('event', 'title')
        unique_together = ('event', 'title')

    def __str__(self):
        return self.title
