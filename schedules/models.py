from django.db import models

from churches.models import Church, Speaker


class Event(models.Model):
    church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='events')
    speakers = models.ManyToManyField(Speaker, related_name='events', blank=True, null=True)
    start_time = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    map_search_query = models.CharField(max_length=300)

    in_person = models.BooleanField(default=True)
    live_stream = models.BooleanField(default=False)
    visibility = models.CharField(choices=(('public', 'Public'), ('members', 'Members Only'), ('hidden', 'Hidden')))

    class Meta:
        ordering = ('start_time', 'church')

    def __str__(self):
        return f'{self.start_time} - {self.title}'
