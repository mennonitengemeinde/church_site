from django.forms import ModelForm, ValidationError

from schedules.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('church', 'start', 'end', 'title', 'description', 'address', 'map_search_query',
                  'in_person', 'live_stream', 'visibility')

    def clean_end(self):
        data = self.cleaned_data['end']
        if data < self.cleaned_data['start']:
            raise ValidationError("End can not be less then Start!")
        return data
