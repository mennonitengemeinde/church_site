from django.db import models

from churches.models import Church
from speakers.models import Speaker

visibility_choices = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('members', 'Members Only'),
)


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

    class Meta:
        ordering = ('start', 'church')

    def __str__(self):
        return self.title
