from django.db import models
from django.conf import settings
import pytz

from contactus.querysets import ContactMessageQuerySet


class ContactMessage(models.Model):
    page_title = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    objects = ContactMessageQuerySet.as_manager()

    class Meta:
        ordering = ['message_date']

    def __str__(self):
        tz = pytz.timezone(settings.TIME_ZONE)
        return self.message_date.astimezone(tz).strftime('%Y-%m-%d, %H:%M:%I %p')
