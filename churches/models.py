from django.db import models

from django_countries.fields import CountryField


class Church(models.Model):
    name = models.CharField(max_length=200, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()

    mixlr_url = models.URLField(null=True, blank=True)

    @property
    def slug(self):
        return self.name.replace(' ', '-').lower()

    class Meta:
        ordering = ('country', 'name')

    def __str__(self):
        return self.name
