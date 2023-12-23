from django.forms import HiddenInput

from churches.models import Church, Choir
from core.forms import CoreModelForm


class ChurchCreateForm(CoreModelForm):
    class Meta:
        model = Church
        fields = ("name", "street", "city", "province_state", "country", "mixlr_url")


class ChoirCreateForm(CoreModelForm):
    class Meta:
        model = Choir
        fields = ["church", "name", "description"]
        widgets = {"church": HiddenInput()}
