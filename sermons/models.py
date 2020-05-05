import os
from django.db import models

from schedules.models import Event
from speakers.models import Speaker

sermon_types = [
    ('message', 'Message'),
    ('opening', 'Opening'),
    ('live_stream', 'Live Stream')
]


def get_audio_path(instance, filename):
    return os.path.join('audio', instance.event.church.name, str(instance.event.start.date()), instance.sermon_type,
                        filename)


class Sermon(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='sermons')
    sermon_type = models.CharField(max_length=50, choices=sermon_types)
    title = models.CharField(max_length=200, null=True, blank=True)
    speaker = models.ManyToManyField(Speaker, related_name='sermons')
    audio_low = models.FileField(upload_to=get_audio_path, null=True, blank=True)
    audio_med = models.FileField(upload_to=get_audio_path, null=True, blank=True)
    audio_high = models.FileField(upload_to=get_audio_path, null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    # Live stream fields
    live_url = models.URLField(blank=True, null=True)
    live = models.BooleanField(default=False)

    class Meta:
        ordering = ('event',)

    def __str__(self):
        return f'{self.sermon_type}'
