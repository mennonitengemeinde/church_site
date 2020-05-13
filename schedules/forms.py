from django.forms import ModelForm, ValidationError

from churches.models import Church
from schedules.models import Event


class EventForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['church'].queryset = Church.objects.filter(members=user, members__membership_validated=True)

    class Meta:
        model = Event
        fields = ('church', 'start', 'end', 'title', 'description', 'address', 'map_search_query',
                  'in_person', 'live_stream', 'visibility')

    def clean_end(self):
        data = self.cleaned_data['end']
        if data < self.cleaned_data['start']:
            raise ValidationError("End can not be less then Start!")
        return data
