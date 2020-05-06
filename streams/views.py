from django.utils import timezone

from church_site.views import BaseListView, BaseDetailView

from .models import Stream


class StreamsListView(BaseListView):
    page_title = 'Live'
    current_page = 'live'
    model = Stream
    template_name = 'streams/streams-list.html'
    context_object_name = 'streams'

    def get_queryset(self):
        return Stream.objects.filter(event__end__gt=timezone.now())


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
