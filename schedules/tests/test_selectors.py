from django.contrib.auth import get_user_model

from schedules.selectors import get_admin_member_attendants
from schedules.tests._setup import EventSetupTestCase

from schedules import selectors


class GetEventsTests(EventSetupTestCase):

    def test_get_events(self):
        events_list = selectors.get_events()
        self.assertEqual(events_list.count(), 3)

    def test_church_filter(self):
        events_list = selectors.get_events(church_name='Church-2')
        self.assertEqual(events_list.count(), 1)

    def test_limit(self):
        events_list = selectors.get_events(limit=1)
        self.assertEqual(events_list.count(), 1)

    def test_desc_order(self):
        events_list = selectors.get_events(church_name='Church-1', order_by_start='desc')
        self.assertEqual(events_list.count(), 2)
        self.assertLess(events_list[0].start, events_list[1].start)

    def test_asc_order(self):
        events_list = selectors.get_events(church_name='Church-1', order_by_start='asc')
        self.assertEqual(events_list.count(), 2)
        self.assertLess(events_list[1].start, events_list[0].start)


class GetAdminEventsTests(EventSetupTestCase):
    def test_get_admin_events(self):
        user = get_user_model().objects.get(username='test_user')

        events_list = selectors.get_admin_events(user=user)
        self.assertEqual(events_list.count(), 4)

    def test_current_events_only(self):
        user = get_user_model().objects.get(username='test_user')
        events_list = selectors.get_admin_events(user=user, current_events_only=True)
        self.assertEqual(events_list.count(), 3)

    def test_desc_order(self):
        user = get_user_model().objects.get(username='test_user')
        events_list = selectors.get_admin_events(user=user, order_by_start='desc')
        self.assertEqual(events_list.count(), 4)
        self.assertLess(events_list[0].start, events_list[1].start)

    def test_asc_order(self):
        user = get_user_model().objects.get(username='test_user')
        events_list = selectors.get_admin_events(user=user, order_by_start='asc')
        self.assertEqual(events_list.count(), 4)
        self.assertLess(events_list[1].start, events_list[0].start)


class AttendantSelectorsTests(EventSetupTestCase):

    def test_get_admin_member_attendants(self):
        user = get_user_model().objects.get(username='test_user')

        attendant_list = get_admin_member_attendants(user=user)
        self.assertEqual(attendant_list.count(), 2)
