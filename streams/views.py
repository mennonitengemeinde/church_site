from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

from church_site.views import AdminListView, BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView
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


class StreamsAdminListView(AdminListView):
    model = Stream
    context_object_name = 'streams'
    template_name = 'streams/streams-admin-list.html'
    page_title = 'Streams - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('streams:streams-admin-create')


class StreamsAdminCreateView(BaseCreateView):
    model = Stream
    template_name = 'admin-form-view.html'
    fields = ('event', 'title', 'description', 'speakers', 'live_url', 'live_mixlr_audio', 'live')
    success_url = reverse_lazy('streams:streams-admin-list')
    page_title = 'New Stream - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('streams:streams-admin-list')


class StreamAdminUpdateView(BaseUpdateView):
    model = Stream
    template_name = 'admin-form-view.html'
    fields = ('event', 'title', 'description', 'speakers', 'live_url', 'live_mixlr_audio', 'live')
    success_url = reverse_lazy('streams:streams-admin-list')
    page_title = 'Update Stream - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('streams:streams-admin-list')


class StreamAdminLiveUpdateView(View):
    def get(self, request, pk=None):
        stream = Stream.objects.filter(id=pk).first()
        if stream:
            stream.live = not stream.live
            stream.save()
        return redirect('streams:streams-admin-list')
