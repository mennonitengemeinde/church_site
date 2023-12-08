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


class Choir(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='choirs', null=True, blank=True)

    church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='choirs')

    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'church')

    def __str__(self):
        return self.name
