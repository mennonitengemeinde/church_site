from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import User
from churches.models import Church


class UsersSetupTestCase(TestCase):
    def create_church(self, name='Church 1', street='street 1', city='City', province_state='State', country='CA'):
        return Church.objects.create(name=name, street=street, city=city, province_state=province_state,
                                     country=country)

    def create_user(self, username: str = 'user_1', church: Church = None):
        user = User.objects.create_user(username)
        if church:
            user.churches.add(church)
        return user

    def setUp(self) -> None:
        church_1 = self.create_church()
        church_2 = self.create_church(name='Church 2')

        self.create_user(church=church_1)
        self.create_user(username='user_2', church=church_2)
        self.create_user(username='user_3', church=church_1)
        User.objects.create_superuser('superuser')
