from church_site.views import BaseListView

from .models import Event


class EventsListView(BaseListView):
    page_title = 'Events'
    current_page = 'events'
    model = Event
    template_name = 'schedules/event-list.html'
    context_object_name = 'events'

