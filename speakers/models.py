from django.db import models

from django_countries.fields import CountryField

from churches.models import Church


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()
    home_church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='speakers')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
