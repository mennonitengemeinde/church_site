from django.utils import timezone

from church_site.views import BaseListView, BaseDetailView
from churches.models import Church

from .models import Stream


class StreamsListView(BaseListView):
    page_title = 'Live'
    current_page = 'live'
    model = Stream
    template_name = 'streams/streams-list.html'
    context_object_name = 'streams'

    def get_queryset(self):
        if self.kwargs.get('church'):
            return self.model.objects.filter(event__end__gt=timezone.now(),
                                             event__church__name=self.kwargs.get('church').replace('-', ' '))
        return Stream.objects.filter(event__end__gt=timezone.now())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['churches'] = Church.objects.all()
        context['current_church'] = self.kwargs.get('church') if self.kwargs.get('church') else None
        return context


class LiveAudioView(BaseDetailView):
    # page_title = 'Page Title'
    current_page = 'live'
    model = Stream
    template_name = 'streams/live-audio.html'
    context_object_name = 'stream'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Live Audio - {self.object.title}'
        return context


class LiveVideoView(BaseDetailView):
    page_title = 'Page Title'
    current_page = 'live'
    model = Stream
    template_name = 'streams/live-video.html'
    context_object_name = 'stream'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Live Video - {self.object.title}'
        return context
