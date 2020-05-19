import os
from django.db import models
from uuid import uuid4

from schedules.models import Event
from sermons.validators import validate_file_extension
from speakers.models import Speaker

sermon_types = [
    ('message', 'Message'),
    ('opening', 'Opening')
]


def low_audio_path(instance, filename):
    return os.path.join(
        'audio',
        instance.event.church.slug,
        str(instance.event.start.date()),
        instance.sermon_type,
        f'{uuid4()}-low.mp3')


def med_audio_path(instance, filename):
    return os.path.join(
        'audio',
        instance.event.church.slug,
        str(instance.event.start.date()),
        instance.sermon_type,
        f'{uuid4()}-low.mp3')


def high_audio_path(instance, filename):
    return os.path.join(
        'audio',
        instance.event.church.slug,
        str(instance.event.start.date()),
        instance.sermon_type,
        f'{uuid4()}-low.mp3')


class SermonQuerySet(models.query.QuerySet):
    def member_sermons(self, user):
        return self.filter(event__church__members=user)


class SermonManager(models.Manager):
    def get_queryset(self):
        return SermonQuerySet(self.model, self._db)

    def filtered_sermons(self, church: str = None, speaker: str = None):
        if church and not speaker:
            return self.filter(visible=True, event__church__name=church.replace('-', ' ')).order_by('-event')
        elif not church and speaker:
            return self.filter(visible=True, speakers=int(speaker)).order_by('-event')
        elif church and speaker:
            return self.filter(visible=True, event__church__name=church.replace('-', ' '), speakers=int(speaker)).order_by('-event')
        else:
            return self.filter(visible=True).order_by('-event')


class Sermon(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='sermons')
    sermon_type = models.CharField(max_length=50, choices=sermon_types)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='sermons')
    audio_low = models.FileField(upload_to=low_audio_path, validators=[validate_file_extension], null=True, blank=True)
    audio_med = models.FileField(upload_to=med_audio_path, validators=[validate_file_extension], null=True, blank=True)
    audio_high = models.FileField(upload_to=high_audio_path, validators=[validate_file_extension], null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    objects = SermonManager()

    class Meta:
        ordering = ('event', 'title')
        unique_together = ('event', 'title')

    def __str__(self):
        return f'{self.sermon_type}-{self.title}'
