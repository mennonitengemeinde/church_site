from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser
from django.db import models

from django_countries.fields import CountryField

from churches.models import Church


class User(AbstractUser):
    country = CountryField()
    churches = models.ManyToManyField(Church, related_name='members')
    # preferred_church = models.ForeignKey(Church, related_name='frequent_visitors', on_delete=models.PROTECT,
    #                                      null=True, blank=True)
