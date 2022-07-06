from django.forms import ModelForm, HiddenInput, TextInput, Textarea
from django_countries.widgets import CountrySelectWidget

from churches.models import Church


class ChurchCreateForm(ModelForm):
    class Meta:
        model = Church
        fields = ('name', 'street', 'city', 'province_state', 'country', 'mixlr_url')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'input input-bordered w-full max-w-xs'}),
            'street': TextInput(attrs={'placeholder': 'Street', 'class': 'input input-bordered w-full max-w-xs'}),
            'city': TextInput(attrs={'placeholder': 'City', 'class': 'input input-bordered w-full max-w-xs'}),
            'province_state': TextInput(
                attrs={'placeholder': 'Province/State', 'class': 'input input-bordered w-full max-w-xs'}),
            'country': CountrySelectWidget(
                attrs={'placeholder': 'Country', 'class': 'select select-bordered w-full max-w-xs'}),
            'mixlr_url': TextInput(attrs={'placeholder': 'Mixlr URL', 'class': 'input input-bordered w-full max-w-xs'}),
        }
