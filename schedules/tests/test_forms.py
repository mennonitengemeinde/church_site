from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from churches.models import Church
from schedules.forms import EventForm
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
