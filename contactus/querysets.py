from django.db import models


class ContactMessageQuerySet(models.QuerySet):
    def all_existing(self):
        return self.filter(deleted=False)
