from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from churches.models import Church
from schedules.models import Event


class EventSetupTestCase(TestCase):
    def create_church(self, name='Church 1', street='street 1', city='City', province_state='State', country='CA'):
        return Church.objects.create(name=name, street=street, city=city, province_state=province_state,
                                     country=country)

    def create_event(self, church, start=timezone.now() + timedelta(days=1), end=timezone.now() + timedelta(days=2),
                     title='Title 1', visibility='public'):
        return Event.objects.create(start=start, end=end, title=title, church=church, visibility=visibility)

    def setUp(self):
        church_1 = self.create_church()
        church_2 = self.create_church(name='Church 2')

        self.user = get_user_model().objects.create_user(username='test_user', password='password')
        self.user.churches.add(church_1)

        self.create_event(church_1)
        self.create_event(church_1, title='Title 2', visibility='private')
        self.create_event(church_1, start=timezone.now() - timedelta(days=2), end=timezone.now() - timedelta(days=1),
                          title='Title 3', visibility='public')
        self.create_event(church_2, title='Title 4')
