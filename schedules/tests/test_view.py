from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from schedules.models import Event
from schedules.tests._setup import EventSetupTestCase


class EventsViewTests(EventSetupTestCase):

    def test_view_returns_200(self):
        resp = self.client.get(reverse('schedules:events-list'))
        self.assertEqual(resp.status_code, 200)

    def test_events(self):
        resp = self.client.get(reverse('schedules:events-list'))
        self.assertEqual(len(resp.context['events']), 3)


class EventsAdminListViewTests(EventSetupTestCase):

    def test_403_if_no_permission(self):
        self.client.login(username='test_user', password='password')
        url = reverse('schedules:events-admin-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 403)

    def test_redirect_anonymous(self):
        url = reverse('schedules:events-admin-list')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url.split('?')[0], reverse('account_login'))

    def test_view_with_permissions(self):
        content_type = ContentType.objects.get_for_model(Event, for_concrete_model=True)
        can_view_event = Permission.objects.filter(content_type=content_type, codename='view_event').first()
        self.user.user_permissions.add(can_view_event)

        self.client.login(username='test_user', password='password')
        url = reverse('schedules:events-admin-list')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['events']), 3)
