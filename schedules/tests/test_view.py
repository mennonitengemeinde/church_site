from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from churches.models import Church
from schedules.models import Event


class ScheduleViewTests(TestCase):

    def create_church(self, name='Church_1', street='street 1', city='City', province_state='State', country='CA'):
        return Church.objects.create(name=name, street=street, city=city, province_state=province_state,
                                     country=country)

    def create_event(self, start=timezone.now() + timedelta(days=1), end=timezone.now() + timedelta(days=2),
                     title='Title 1', visibility='public'):
        return Event.objects.create(start=start, end=end, title=title, visibility=visibility)

    def setUp(self):
        self.church = self.create_church()
        self.user = get_user_model().objects.create(username='test_user')
        self.user.churches.add(self.church)

    def test_event_admin_view(self):
        event = self.create_event()
        event.church = self.church
        event.save()
        return True
