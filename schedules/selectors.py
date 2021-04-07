from typing import Iterable

from django.utils import timezone

from schedules.models import Event, Attendant


def get_member_only_events(user: int, reverse_order: bool = False) -> Iterable[Event]:
    if reverse_order:
        return Event.objects.filter(church__members=user, end__gt=timezone.now()).order_by('start')
    else:
        return Event.objects.filter(church__members=user).order_by('-start')


def get_admin_member_attendants(user: int) -> Iterable[Attendant]:
    return Attendant.objects.filter(event__church__members=user)


def get_event_list(church_name: str = None, limit: int = None) -> Iterable[Event]:
    if church_name:
        if limit:
            return Event.objects.filter(
                visibility='public', end__gt=timezone.now(), church__name__iexact=church_name.replace('-', ' '))[:limit]
        return Event.objects.filter(visibility='public', end__gt=timezone.now(), church__name__iexact=church_name.replace('-', ' '))
    else:
        if limit:
            return Event.objects.filter(visibility='public', end__gt=timezone.now())[:limit]
        return Event.objects.filter(visibility='public', end__gt=timezone.now())
