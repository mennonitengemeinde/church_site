from django.db import models

from django_countries.fields import CountryField


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
