from django.db import models

from churches.models import Church
from speakers.models import Speaker


class Event(models.Model):
    church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='events')
    speakers = models.ManyToManyField(Speaker, related_name='events', blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    map_search_query = models.CharField(max_length=300, blank=True, null=True)

    in_person = models.BooleanField(default=True)
    live_stream = models.BooleanField(default=False)
    visibility = models.CharField(max_length=50, choices=(
        ('public', 'Public'), ('members', 'Members Only'), ('hidden', 'Hidden')))

    class Meta:
        ordering = ('start', 'church')

    def __str__(self):
        return self.title
