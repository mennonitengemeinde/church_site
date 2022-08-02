from core.forms import CoreModelForm
from speakers.models import Speaker


class SpeakerCreateForm(CoreModelForm):
    class Meta:
        model = Speaker
        fields = ('name', 'city', 'province_state', 'country', 'home_church')
