from django.forms import ModelForm

from schedules.models import Event
from sermons.models import Sermon


class SermonCreateForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.member_only_events(user=user).order_by('-start')

    class Meta:
        model = Sermon
        fields = ('event', 'sermon_type', 'title', 'description', 'speakers', 'video_url',
                  'audio_low', 'audio_med', 'audio_high', 'visible')
