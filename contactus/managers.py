from django.db import models


class ContactMessageManager(models.Manager):
    def get_queryset(self):
        return self.filter(deleted=False)
