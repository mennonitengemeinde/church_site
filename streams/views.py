from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from church_site.views import AdminListView, BaseDetailView, BaseCreateView, BaseUpdateView
from .forms import StreamCreateForm

from .models import Stream
from .selectors import get_live_streams, get_member_streams, get_member_stream


class StreamsListView(View):
    def get(self, request):
        context = {
            'page_title': 'Live - Mennoniten Gemeinde',
            'current_page': 'live',
        }
        return render(request, 'streams/streams-list-apline.html', context)


class LiveAudioView(BaseDetailView):
    # page_title = 'Page Title'
    current_page = 'live'
    model = Stream
    template_name = 'streams/live-audio.html'
    context_object_name = 'stream'
    queryset = get_live_streams()

    def get_context_data(self, **kwargs):
        context = super(LiveAudioView, self).get_context_data(**kwargs)
        context['page_title'] = f'Live Audio - {self.object.title}'
        try:
            context['stream'].audio_views += 1
            context['stream'].save()
        except Exception as e:
            print('Error', e)
        return context

    # def get_queryset(self):
    #     return self.model.objects.filter(live=True)


class LiveVideoView(BaseDetailView):
    page_title = 'Page Title'
    current_page = 'live'
    model = Stream
    template_name = 'streams/live-video.html'
    context_object_name = 'stream'
    queryset = get_live_streams()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Live Video - {self.object.title}'
        try:
            context['stream'].video_views += 1
            context['stream'].save()
        except Exception as e:
            print('Error', e)
        return context

    # def get_queryset(self):
    #     return self.model.objects.filter(live=True)


class StreamsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'streams.view_stream'
    model = Stream
    context_object_name = 'streams'
    template_name = 'streams/streams-admin-list.html'
    page_title = 'Streams - Admin'
    current_page = 'admin_streams'
    btn_add_href = reverse_lazy('streams:streams-admin-create')
    paginate_by = 5

    def get_queryset(self):
        return get_member_streams(self.request.user, True)

    def get_template_names(self):
        if self.request.htmx:
            self.template_name = 'streams/partials/stream-admin-list-partial.html'
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagination_links'] = self.get_pagination_links(context['page_obj'])
        return context


class StreamsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'streams.add_stream'
    model = Stream
    template_name = 'admin-form-view.html'
    form_class = StreamCreateForm
    success_url = reverse_lazy('streams:streams-admin-list')
    page_title = 'New Stream - Admin'
    current_page = 'admin_streams'
    btn_back_href = reverse_lazy('streams:streams-admin-list')

    def get_queryset(self):
        return get_member_streams(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StreamAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'streams.change_stream'
    model = Stream
    template_name = 'admin-form-view.html'
    form_class = StreamCreateForm
    success_url = reverse_lazy('streams:streams-admin-list')
    page_title = 'Update Stream - Admin'
    current_page = 'admin_streams'
    btn_back_href = reverse_lazy('streams:streams-admin-list')

    def get_queryset(self):
        return get_member_streams(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StreamAdminLiveUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'streams.change_stream'
    http_method_names = ['post']
    model = Stream
    fields = ['live']
    success_url = reverse_lazy('streams:streams-admin-list')

    def get_queryset(self):
        return get_member_streams(self.request.user)
