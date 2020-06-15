from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser
from django.db import models

from django_countries.fields import CountryField

from churches.models import Church


class User(AbstractUser):
    country = CountryField()
    member = models.ManyToManyField(Church, related_name='members')

    @property
    def is_validated(self):
        email = EmailAddress.objects.filter(user=self, verified=True)
        if email:
            return True
        else:
            return False
