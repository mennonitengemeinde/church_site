from django.db import models
from django.utils import timezone


class AttendantManager(models.Manager):
    def get_member_attendants(self, user):
        return self.filter(event__church__members=user)


class EventManager(models.Manager):
    def get_first_six(self):
        return self.get_queryset().filter(end__gt=timezone.now())[:6]

    def get_first_twelve(self):
        return self.get_queryset().filter(end__gt=timezone.now())[:12]

    def current_memeber_only_events(self, user):
        return self.filter(church__members=user, end__gt=timezone.now())

    def member_only_events(self, user):
        return self.get_queryset().filter(church__members=user)
