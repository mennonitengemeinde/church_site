from django.forms import ModelForm

from schedules.selectors import get_member_only_events
from sermons.models import Sermon


class SermonCreateForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(SermonCreateForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = get_member_only_events(user=user, reverse_order=True)

    class Meta:
        model = Sermon
        fields = ('event', 'sermon_type', 'title', 'description', 'speakers', 'video_url',
                  'audio_low', 'audio_med', 'audio_high', 'visible')
