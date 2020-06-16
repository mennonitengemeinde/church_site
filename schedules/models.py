import pytz
from django.conf import settings
from django.core.validators import MinValueValidator
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

    def get_first_twelve(self):
        return self.get_queryset().filter(end__gt=timezone.now())[:12]

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
    attendance_limit = models.IntegerField(default=0)
    attendance_signup = models.BooleanField(default=False)
    visibility = models.CharField(max_length=50, choices=visibility_choices)

    objects = EventManager()

    @property
    def available_attendance(self):
        if self.attendance_limit == 0:
            return 0
        else:
            total_count = 0
            for attendant in self.attendants.all():
                total_count = total_count + attendant.amount
            return self.attendance_limit - total_count

    @property
    def total_attendants(self):
        total_sum = 0
        for attendant in self.attendants.all():
            total_sum = total_sum + attendant.amount
        return total_sum

    class Meta:
        ordering = ('start', 'church')

    def __str__(self):
        local_timezone = pytz.timezone(settings.TIME_ZONE)
        local_date = self.start.astimezone(local_timezone)
        return f'{local_date.strftime("%G-%m-%d %I:%M%p")} - {self.church.name} - {self.title}'


class AttendantManager(models.Manager):
    def get_member_attendants(self, user):
        return self.filter(event__church__members=user)


class Attendant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='attendants')
    full_name = models.CharField(max_length=150)
    amount = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    objects = AttendantManager()

    class Meta:
        ordering = ('event', 'full_name')

    def __str__(self):
        return f'{self.event} - {self.full_name}'
