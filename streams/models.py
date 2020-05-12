from django.db import models

from speakers.models import Speaker
from schedules.models import Event


class StreamQuerySet(models.query.QuerySet):
    def member_streams(self, user):
        return self.filter(event__church__members=user, event__church__members__membership_validated=True)


class StreamManager(models.Manager):
    def get_queryset(self):
        return StreamQuerySet(self.model, self._db)

    def member_only_streams(self, user):
        return self.get_queryset().filter(event__church__members=user, event_church__members__membership_validated=True)


class Stream(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='streams')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='streams')
    live_url = models.URLField(blank=True, null=True)
    live_mixlr_audio = models.BooleanField(default=False)
    live = models.BooleanField(default=False)

    objects = StreamManager()

    class Meta:
        ordering = ('event', 'title')
        unique_together = ('event', 'title')

    def __str__(self):
        return self.title
