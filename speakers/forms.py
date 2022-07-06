from django.forms import ModelForm, TextInput
from django_countries.widgets import CountrySelectWidget

from speakers.models import Speaker


class SpeakerCreateForm(ModelForm):
    class Meta:
        model = Speaker
        fields = ('name', 'city', 'province_state', 'country', 'home_church')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'input input-bordered w-full max-w-sm'}),
            'city': TextInput(attrs={'placeholder': 'City', 'class': 'input input-bordered w-full max-w-sm'}),
            'province_state': TextInput(
                attrs={'placeholder': 'Province/State', 'class': 'input input-bordered w-full max-w-sm'}),
            'country': CountrySelectWidget(
                attrs={'placeholder': 'Country', 'class': 'select select-bordered w-full max-w-sm'}),
            'home_church': TextInput(
                attrs={'placeholder': 'Home Church', 'class': 'input input-bordered w-full max-w-sm'}),
        }
