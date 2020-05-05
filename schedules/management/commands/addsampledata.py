from datetime import timedelta
from django.core.management import BaseCommand
from django.utils import timezone
from random import randint

from churches.models import Church
from speakers.models import Speaker
from schedules.models import Event

description = ('', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam dictum bibendum lacus, '
                   'at tristique leo. Integer rutrum pharetra quam vitae tempor. Vivamus eget scelerisque nulla, '
                   'sit amet hendrerit odio. Donec vestibulum auctor ante, vitae lobortis sem. Pellentesque '
                   'pellentesque dictum arcu, semper dictum mi posuere id. In condimentum mi sapien, a malesuada '
                   'purus accumsan quis. Vivamus vehicula magna non lacus egestas elementum. Donec sem urna, '
                   'venenatis vitae consequat a, varius vel orci. Aliquam nec tincidunt enim. Pellentesque rutrum '
                   'odio vel est finibus blandit. Pellentesque non ipsum urna. Etiam eros sapien, dapibus sed '
                   'tempus vitae, mollis in est.')


def create_churches():
    Church.objects.create(name='Church 1', street='7642 S. High Road', city='Westland', province_state='Michigan',
                          country='US')
    Church.objects.create(name='Church 2', street='46 Shadow Brook Street', city='Naples', province_state='Florida',
                          country='US')
    Church.objects.create(name='Church 3', street='13 San Carlos St.', city='Christiansburg', province_state='Virginia',
                          country='US')
    Church.objects.create(name='Church 4', street='489 Maple Ave.', city='Frankfort', province_state='Kentucky',
                          country='US')


def create_speakers():
    Speaker.objects.create(name='Sam Williams', city='Westland', province_state='Michigan', country='US')
    Speaker.objects.create(name='Brian Walker', city='Naples', province_state='Florida', country='US')
    Speaker.objects.create(name='Bill Murphy', city='Christiansburg', province_state='Virginia', country='US')
    Speaker.objects.create(name='Tim Johnson', city='Frankfort', province_state='Kentucky', country='US')


def create_events():
    hours = (
        {'start_hour': 9, 'start_minute': 30, 'end_hour': 11, 'end_minute': 0},
        {'start_hour': 19, 'start_minute': 30, 'end_hour': 21, 'end_minute': 0},
        {'start_hour': 14, 'start_minute': 00, 'end_hour': 16, 'end_minute': 0},
        {'start_hour': 19, 'start_minute': 00, 'end_hour': 20, 'end_minute': 30},
    )

    for i in range(20):
        hour = hours[randint(0, len(hours) - 1)]

        create_event(
            title=f'Event {i}',
            start_days_added=randint(0, 15),
            start_hour=hour['start_hour'],
            start_minute=hour['start_minute'],
            end_hour=hour['end_hour'],
            end_minute=hour['end_minute']
        )


def create_event(title: str, start_days_added: int, start_hour: int, start_minute: int,
                 end_hour: int, end_minute: int, desc=None, address=None):
    churches = Church.objects.all()
    date = timezone.now() + timedelta(days=start_days_added)
    end_date = date.replace(hour=end_hour, minute=end_minute)
    start_date = date.replace(hour=start_hour, minute=start_minute)
    church = churches[randint(0, len(churches) - 1)]
    use_church_address = bool(randint(0, 1))
    if address:
        local_address = address
    else:
        if use_church_address:
            local_address = f'{church.street}\n{church.city}, {church.province_state}, {church.country}'
        else:
            local_address = ''

    event = Event(
        church=church,
        start=start_date,
        end=end_date,
        title=title,
        description=desc or description[randint(0, 1)],
        address=local_address,
        map_search_query=f'{church.street} {church.city} {church.province_state} {church.country}' if use_church_address else '',
        in_person=True if local_address is not '' else False,
        live_stream=bool(randint(0, 1)),
        visibility='public'
    )

    event.save()


class Command(BaseCommand):
    help = 'Adds sample data'

    def handle(self, *args, **options):
        create_churches()
        self.stdout.write(self.style.SUCCESS('Successfully created churches'))
        create_speakers()
        self.stdout.write(self.style.SUCCESS('Successfully created speakers'))
        create_events()
        self.stdout.write(self.style.SUCCESS('Successfully created events'))
