from django.contrib.auth import get_user_model

from accounts.models import User
from accounts.selectors import get_users_from_same_church
from accounts.tests._setup import UsersSetupTestCase


class GetUsersFromSameChurchTests(UsersSetupTestCase):

    def test_user_belonging_to_church(self):
        u = User.objects.filter(username='user_1').first()
        u_list = get_users_from_same_church(u)
        self.assertEqual(u_list.count(), 3)

    def test_user_not_belonging_to_church(self):
        u = User.objects.filter(username='user_2').first()
        u_list = get_users_from_same_church(u)
        self.assertEqual(u_list.count(), 2)
