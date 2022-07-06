from django.contrib import messages
from django.forms import ModelForm, ValidationError, HiddenInput, Select, TextInput, Textarea, CheckboxInput

from churches.models import Church
from schedules.models import Event, Attendant


class EventForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['church'].queryset = Church.objects.filter(members=user)

    class Meta:
        model = Event
        fields = ('church', 'start', 'end', 'title', 'description', 'address', 'map_search_query',
                  'in_person', 'live_stream', 'attendance_limit', 'attendance_signup', 'visibility')
        widgets = {
            'church': Select(attrs={'class': 'select select-bordered w-full max-w-xs'}),
            'start': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'end': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'title': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'description': Textarea(attrs={'class': 'textarea textarea-bordered w-full h-20 max-w-xs'}),
            'address': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'map_search_query': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'in_person': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'live_stream': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'attendance_limit': TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'attendance_signup': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'visibility': Select(attrs={'class': 'select select-bordered w-full max-w-xs'}),
        }

    def clean_end(self):
        data = self.cleaned_data['end']
        if data < self.cleaned_data['start']:
            raise ValidationError("End can not be less then Start!")
        return data


class AttendantAdminForm(ModelForm):
    class Meta:
        model = Attendant
        fields = ('event', 'full_name', 'amount')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        event = self.cleaned_data.get('event')
        available = event.available_attendance + self.instance.amount
        if available < amount:
            raise ValidationError(f'There are only {available} spaces available')

        return self.cleaned_data['amount']


class AttendantForm(AttendantAdminForm):
    class Meta:
        model = Attendant
        fields = ('event', 'full_name', 'amount')
        widgets = {
            'event': HiddenInput()
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        event = self.cleaned_data.get('event')
        available = event.available_attendance
        if available < amount:
            raise ValidationError(f'There are only {available} spaces available')

        return self.cleaned_data['amount']
