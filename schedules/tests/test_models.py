import pytz
from django.conf import settings

from schedules.models import Event, Attendant
from schedules.tests._setup import EventSetupTestCase


class EventTests(EventSetupTestCase):

    def test_event_str(self):
        e = Event.objects.get(title='Title 5')
        local_timezone = pytz.timezone(settings.TIME_ZONE)
        n = e.start.astimezone(local_timezone).strftime("%G-%m-%d %I:%M%p")
        self.assertEqual(str(e), f'{n} - Church 1 - Title 5')


class AttendantTests(EventSetupTestCase):
    def test_attendant_str(self):
        a = Attendant.objects.get(full_name='Attendant 1')
        e = Event.objects.get(title='Title 5')
        local_timezone = pytz.timezone(settings.TIME_ZONE)
        n = e.start.astimezone(local_timezone).strftime("%G-%m-%d %I:%M%p")
        self.assertEqual(str(a), f'{n} - Church 1 - Title 5 - Attendant 1')
