from random import randint

from churches.models import Church
from speakers.models import Speaker


def create_speakers():
    churches = Church.objects.all()
    Speaker.objects.create(name='Sam Williams', city='Westland', province_state='Michigan', country='US',
                           home_church=churches[randint(0, len(churches)-1)])
    Speaker.objects.create(name='Brian Walker', city='Naples', province_state='Florida', country='US',
                           home_church=churches[randint(0, len(churches)-1)])
    Speaker.objects.create(name='Bill Murphy', city='Christiansburg', province_state='Virginia', country='US',
                           home_church=churches[randint(0, len(churches)-1)])
    Speaker.objects.create(name='Tim Johnson', city='Frankfort', province_state='Kentucky', country='US',
                           home_church=churches[randint(0, len(churches)-1)])
