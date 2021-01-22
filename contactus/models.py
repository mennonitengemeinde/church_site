from django.db import models


class ContactMessage(models.Model):
    page_title = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(null=True, blank=True)
    message_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(False)

    class Meta:
        ordering = ['message_date']

    def __str__(self):
        return self.message_date
