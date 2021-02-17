from typing import Iterable

from django.utils import timezone

from schedules.models import Event, Attendant


def get_admin_member_only_events(user: int, current: bool = False) -> Iterable[Event]:
    if current:
        return Event.objects.filter(church__members=user, end__gt=timezone.now()).order_by('start')
    else:
        return Event.objects.filter(church__members=user).order_by('-start')


def get_admin_member_attendants(user: int) -> Iterable[Attendant]:
    return Attendant.objects.filter(event__church__members=user)


def get_event_list(church_name: str = None) -> Iterable[Event]:
    if church_name:
        return Event.objects.filter(visibility='public', end__gt=timezone.now(), church__name__iexact=church_name.replace('-', ' '))
    else:
        return Event.objects.filter(visibility='public', end__gt=timezone.now())
