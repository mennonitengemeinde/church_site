from core.forms import CoreModelForm
from schedules.selectors import get_admin_events
from sermons.models import Sermon


class SermonCreateForm(CoreModelForm):
    def __init__(self, user, *args, **kwargs):
        super(SermonCreateForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = get_admin_events(user=user, order_by_start='asc')

    class Meta:
        model = Sermon
        fields = ('event', 'sermon_type', 'title', 'description', 'speakers', 'video_url',
                  'audio_low', 'audio_med', 'audio_high', 'og_image', 'visible')
