from core.forms import CoreModelForm
from songs.models import Choir


class ChoirCreateForm(CoreModelForm):
    class Meta:
        model = Choir
        fields = ['church', 'name', 'description', 'image']
        