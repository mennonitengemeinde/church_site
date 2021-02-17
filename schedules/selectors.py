from typing import Iterable

from django.utils import timezone

from schedules.models import Event


def get_event_list(church: int = None) -> Iterable[Event]:
    if church:
        return Event.objects.filter(end__gt=timezone.now(), church__name=self.kwargs.get('church').replace('-', ' '))
    else:
        return Event.objects.filter(end__gt=timezone.now())
