from accounts.models import User
from streams.models import Stream


def get_live_streams():
    return Stream.objects.filter(live=True)


def get_member_streams(user: User, reverse_order: bool = None):
    queryset = Stream.objects.filter(event__church__members=user).prefetch_related('event')
    if reverse_order:
        return queryset.order_by('-event')
    return queryset


def get_member_stream(user: User, stream_id: int):
    return Stream.objects.filter(event__church__members=user, id=stream_id).first()
