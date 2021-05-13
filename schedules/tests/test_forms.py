from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from churches.models import Church
from schedules.forms import EventForm, AttendantAdminForm, AttendantForm
from schedules.models import Event, Attendant
from schedules.tests._setup import EventSetupTestCase


class EventFormTests(EventSetupTestCase):

    def test_init(self):
        user = get_user_model().objects.get(username='test_user')
        form = EventForm(user=user)
        self.assertEqual(form.fields['church'].queryset.count(), 1)

    def test_invalid_clean_end(self):
        user = get_user_model().objects.get(username='test_user')
        church = Church.objects.get(name='Church 1')
        data = {'church': church, 'start': timezone.now(), 'end': timezone.now() - timedelta(days=1),
                'title': 'Test', 'visibility': 'public', 'attendance_limit': 0}
        form = EventForm(user=user, data=data)
        self.assertFalse(form.is_valid())

    def test_valid_clean_end(self):
        user = get_user_model().objects.get(username='test_user')
        church = Church.objects.get(name='Church 1')
        data = {'church': church, 'start': timezone.now(), 'end': timezone.now() + timedelta(days=1),
                'title': 'Test', 'visibility': 'public', 'attendance_limit': 0}
        form = EventForm(user=user, data=data)
        self.assertTrue(form.is_valid())


class AttendantAdminFormTests(EventSetupTestCase):

    def test_valid_clean_amount(self):
        e = Event.objects.get(title='Title 5')
        a = Attendant.objects.get(full_name='Attendant 1')
        data = {'event': e, 'full_name': 'Attendant 5', 'amount': 2}
        form = AttendantAdminForm(instance=a, data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_clean_amount(self):
        e = Event.objects.get(title='Title 5')
        a = Attendant.objects.get(full_name='Attendant 1')
        data = {'event': e, 'full_name': 'Attendant 5', 'amount': 4}
        form = AttendantAdminForm(instance=a, data=data)
        self.assertFalse(form.is_valid())


class AttendantFormTests(EventSetupTestCase):

    def test_valid_clean_amount(self):
        e = Event.objects.get(title='Title 5')
        data = {'event': e, 'full_name': 'Attendant 5', 'amount': 1}
        form = AttendantForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_clean_amount(self):
        e = Event.objects.get(title='Title 5')
        data = {'event': e, 'full_name': 'Attendant 5', 'amount': 2}
        form = AttendantForm(data=data)
        self.assertFalse(form.is_valid())

