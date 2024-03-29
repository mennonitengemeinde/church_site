from core.forms import CoreModelForm
from schedules.selectors import get_admin_events
from streams.models import Stream


class StreamCreateForm(CoreModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = get_admin_events(user=user, order_by_start='asc', current_events_only=True)

    class Meta:
        model = Stream
        fields = ('event', 'title', 'description', 'speakers', 'live_url', 'live_mixlr_audio', 'live')
