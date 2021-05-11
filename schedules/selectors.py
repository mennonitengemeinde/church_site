from typing import Iterable

from django.db.models import QuerySet
from django.utils import timezone

from accounts.models import User
from schedules.models import Event, Attendant


def get_events(church_name: str = None, limit: int = None, order_by_start: str = None) -> QuerySet[Event]:
    event_list = Event.objects.filter(visibility='public', end__gt=timezone.now())
    if church_name:
        event_list = event_list.filter(church__name__iexact=church_name.replace('-', ' '))
    if order_by_start:
        if order_by_start == 'desc':
            event_list = event_list.order_by('start')
        elif order_by_start == 'asc':
            event_list = event_list.order_by('-start')
    if limit:
        return event_list[:limit]
    return event_list


def get_admin_events(user: User, current_events_only: bool = False, order_by_start: str = None) -> QuerySet[Event]:
    event_list: QuerySet[Event] = Event.objects.filter(church__members=user)

    if current_events_only:
        event_list = event_list.filter(end__gt=timezone.now())

    if order_by_start:
        if order_by_start == 'desc':
            event_list = event_list.order_by('start')
        elif order_by_start == 'asc':
            event_list = event_list.order_by('-start')

    return event_list


def get_admin_member_attendants(user: User) -> QuerySet[Attendant]:
    """
    Returns all attendants of church where user is member
    """
    return Attendant.objects.filter(event__church__members=user)
