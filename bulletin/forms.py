from bulletin.models import Bulletin
from core.forms import CoreModelForm


class BulletinCreateForm(CoreModelForm):
    class Meta:
        model = Bulletin
        fields = ('year', 'week')
