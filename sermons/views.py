from django.urls import reverse_lazy

from church_site.views import BaseListView, BaseDetailView

from churches.models import Church
from schedules.models import Event
from speakers.models import Speaker


class SermonsListView(BaseListView):
    page_title = 'Sermons'
    current_page = 'sermons'
    model = Event
    template_name = 'sermons/sermons-list.html'
    context_object_name = 'events'

    def get_queryset(self):
        print()
        if self.kwargs.get('church'):
            if self.request.GET.get('speaker'):
                return self.model.objects.filter(sermons__isnull=False,
                                                 church__name=self.kwargs['church'].replace('-', ' '),
                                                 sermons__speakers=int(self.request.GET.get('speaker')))
            return self.model.objects.filter(sermons__isnull=False,
                                             church__name=self.kwargs['church'].replace('-', ' '))
        else:
            if self.request.GET.get('speaker'):
                return self.model.objects.filter(sermons__isnull=False,
                                                 sermons__speakers=int(self.request.GET.get('speaker')))
            return self.model.objects.filter(sermons__isnull=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_church'] = self.kwargs.get('church') if self.kwargs.get('church') else None
        context['current_speaker'] = int(self.request.GET.get('speaker')) if self.request.GET.get('speaker') else None
        context['churches'] = Church.objects.all()
        context['speakers'] = Speaker.objects.all()
        return context


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
