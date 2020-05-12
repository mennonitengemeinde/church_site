from django.forms import ModelForm

from schedules.models import Event
from streams.models import Stream


class StreamCreateForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.member_only_events(user=user)

    class Meta:
        model = Stream
        fields = ('event', 'title', 'description', 'speakers', 'live_url', 'live_mixlr_audio', 'live')
