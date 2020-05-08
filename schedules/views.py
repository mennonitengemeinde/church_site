from church_site.views import BaseListView
from churches.models import Church

from .models import Event


class EventsListView(BaseListView):
    page_title = 'Events'
    current_page = 'events'
    model = Event
    template_name = 'schedules/event-list.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.kwargs.get('church'):
            return self.model.objects.filter(church__name=self.kwargs.get('church').replace('-', ' '))
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_church'] = self.kwargs.get('church') if self.kwargs.get('church') else None
        context['churches'] = Church.objects.all()
        return context
