from django.forms import ModelForm, Select, TextInput, Textarea, CheckboxInput, SelectMultiple

from schedules.models import Event
from schedules.selectors import get_admin_events
from streams.models import Stream


class StreamCreateForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = get_admin_events(user=user, order_by_start='asc')

    class Meta:
        model = Stream
        fields = ('event', 'title', 'description', 'speakers', 'live_url', 'live_mixlr_audio', 'live')
        widgets = {
            'event': Select(attrs={'class': 'select select-bordered w-full max-w-sm'}),
            'title': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'description': Textarea(attrs={'class': 'textarea textarea-bordered w-full h-20 max-w-sm'}),
            'speakers': SelectMultiple(attrs={'class': 'select select-bordered select-multiple w-full max-w-sm'}),
            'live_url': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'live_mixlr_audio': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'live': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
        }
