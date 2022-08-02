from churches.models import Church
from core.forms import CoreModelForm


class ChurchCreateForm(CoreModelForm):
    class Meta:
        model = Church
        fields = ('name', 'street', 'city', 'province_state', 'country', 'mixlr_url')
