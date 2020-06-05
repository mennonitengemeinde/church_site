from django.db import models
from django.utils import timezone

from churches.models import Church
from speakers.models import Speaker

visibility_choices = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('members', 'Members Only'),
)


class EventQuerySet(models.query.QuerySet):
    def member_events(self, user):
        return self.filter(church__members=user)


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)

    def get_first_six(self):
        return self.get_queryset().filter(end__gt=timezone.now())[:6]

    def member_only_events(self, user):
        return self.get_queryset().filter(church__members=user)


class Event(models.Model):
    church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='events')
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    map_search_query = models.CharField(max_length=300, blank=True, null=True)

    in_person = models.BooleanField(default=True)
    live_stream = models.BooleanField(default=False)
    visibility = models.CharField(max_length=50, choices=visibility_choices)

    objects = EventManager()

    class Meta:
        ordering = ('start', 'church')

    def __str__(self):
        return f'{self.start.date()} - {self.title}'
