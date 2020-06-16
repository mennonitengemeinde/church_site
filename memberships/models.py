from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

from churches.models import Church

marital_status = (
    (0, 'Single'),
    (1, 'Married'),
)


class Membership(models.Model):
    church = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='membership')
    person = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='memberships')
    start_date = models.DateField()
    reason_for_joining = models.TextField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)
    reason_for_leaving = models.TextField(null=True, blank=True)
    verse = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.church} - {self.person} - {self.start_date}'


class Family(models.Model):
    name = models.CharField(max_length=200, unique=True)
    father = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='father_of')
    mother = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='mother_of')

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, related_name='member_info',
                                blank=True, null=True)
    first_name = models.CharField(max_length=100)
    first_last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    date_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()
    marital_status = models.IntegerField(max_length=50, choices=marital_status)
    passed_away = models.ForeignKey('Family', on_delete=models.PROTECT, related_name='passed_away',
                                    null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    member_of = models.ForeignKey(Church, on_delete=models.PROTECT, related_name='church_members')
    speaker = models.BooleanField(default=False)
    spouse = models.OneToOneField('Person', on_delete=models.PROTECT, related_name='spouse', blank=True, null=True)
    child_of = models.ForeignKey(Family, on_delete=models.PROTECT, related_name='children', blank=True, null=True)

    def __str__(self):
        if self.second_last_name:
            return f'{self.first_name} {self.first_last_name} {self.second_last_name}'
        return f'{self.first_name} {self.first_last_name}'
