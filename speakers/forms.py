from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Submit
from django.forms import ModelForm

from speakers.models import Speaker


class SpeakerCreateForm(ModelForm):
    class Meta:
        model = Speaker
        fields = ('name', 'city', 'province_state', 'country')
