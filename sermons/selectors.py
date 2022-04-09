from accounts.models import User
from sermons.models import Sermon


def get_filtered_sermons(church: str = None, speaker: str = None):
    if church and not speaker:
        return Sermon.objects.filter(visible=True, event__church__name__iexact=church.replace('-', ' ')).order_by('-event')
    elif not church and speaker:
        return Sermon.objects.filter(visible=True, speakers=int(speaker)).order_by('-event')
    elif church and speaker:
        return Sermon.objects.filter(
            visible=True, event__church__name__iexact=church.replace('-', ' '), speakers=int(speaker)
        ).order_by('-event')
    else:
        return Sermon.objects.filter(visible=True).order_by('-event')


def get_random_sermons(church: str = None, speaker: str = None, limit: int = None):
    queryset = get_filtered_sermons(church, speaker)
    if limit:
        return queryset.order_by('?')[:limit]
    return queryset.order_by('?')


def get_member_sermons(user: User, reverse_order: bool = False):
    queryset = Sermon.objects.filter(event__church__members=user)
    if reverse_order:
        return queryset.order_by('-event')
    return queryset
