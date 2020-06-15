from django.db import models

from django_countries.fields import CountryField


class ChurchQuerySet(models.query.QuerySet):
    def is_member(self, user):
        return self.filter(members=user)


class ChurchManager(models.Manager):
    def get_queryset(self):
        return ChurchQuerySet(self.model, using=self._db)

    def get_member_churches(self, user):
        return self.filter(members=user)


class Church(models.Model):
    name = models.CharField(max_length=200, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()

    mixlr_url = models.URLField(null=True, blank=True)

    objects = ChurchManager()

    @property
    def slug(self):
        return self.name.replace(' ', '-')

    class Meta:
        ordering = ('country', 'name')

    def __str__(self):
        return self.name
