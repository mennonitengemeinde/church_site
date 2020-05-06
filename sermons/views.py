from django.urls import reverse_lazy

from church_site.views import BaseListView, BaseDetailView

from schedules.models import Event


class SermonsListView(BaseListView):
    page_title = 'Sermons'
    current_page = 'sermons'
    model = Event
    template_name = 'sermons/sermons-list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return self.model.objects.filter(sermons__isnull=False)


class SermonsDetailView(BaseDetailView):
    current_page = 'sermons'
    btn_back_href = reverse_lazy('sermons:sermons-list')
    model = Event
    template_name = 'sermons/sermons-detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'{self.object.start.date()} | {self.object.title}'
        return context
