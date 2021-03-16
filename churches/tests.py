from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from churches.models import Church
from churches.selectors import get_member_churches


class ChurchesTest(TestCase):
    def create_churches(self, name='Church 1', street='123 Street', city='City One', province='State', country='CA',
                        mixlr_url=None):
        return Church.objects.create(name=name, street=street, city=city, province_state=province, country=country,
                                     mixlr_url=mixlr_url)

    def test_church_model(self):
        church = self.create_churches()
        self.assertEqual(church.slug, 'church-1')
        self.assertEqual(str(church), 'Church 1')

    def test_get_member_churches_selector(self):
        user = get_user_model()
        u = user.objects.create(username='test', email='test@test.com', password='password')
        c = self.create_churches()
        self.create_churches(name='Church 2')
        u.churches.add(c)
        res = get_member_churches(u)

        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].name, 'Church 1')

