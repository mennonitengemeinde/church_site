from django.forms import ModelForm, Select, TextInput, Textarea, CheckboxInput, SelectMultiple

from schedules.selectors import get_admin_events
from sermons.models import Sermon


class SermonCreateForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(SermonCreateForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = get_admin_events(user=user, order_by_start='asc')

    class Meta:
        model = Sermon
        fields = ('event', 'sermon_type', 'title', 'description', 'speakers', 'video_url',
                  'audio_low', 'audio_med', 'audio_high', 'visible')
        widgets = {
            'event': Select(attrs={'class': 'select select-bordered w-full max-w-xs'}),
            'sermon_type': Select(attrs={'class': 'select select-bordered w-full max-w-xs'}),
            'title': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'description': Textarea(attrs={'class': 'textarea textarea-bordered w-full h-20 max-w-xs'}),
            'speakers': SelectMultiple(attrs={'class': 'select select-bordered select-multiple w-full max-w-xs'}),
            'video_url': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'audio_low': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'audio_med': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'audio_high': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'visible': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
        }
