from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from church_site.views import BaseListView, BaseDetailView, BaseCreateView, AdminListView, BaseUpdateView

from churches.models import Church
from schedules.models import Event
from sermons.forms import SermonCreateForm
from sermons.models import Sermon
from speakers.models import Speaker


class SermonsListView(BaseListView):
    page_title = 'Sermons'
    current_page = 'sermons'
    model = Event
    template_name = 'sermons/sermons-list.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.kwargs.get('church'):
            if self.request.GET.get('speaker'):
                return self.model.objects.filter(sermons__isnull=False,
                                                 church__name=self.kwargs['church'].replace('-', ' '),
                                                 sermons__speakers=int(self.request.GET.get('speaker'))).order_by('-start')
            return self.model.objects.filter(sermons__isnull=False,
                                             church__name=self.kwargs['church'].replace('-', ' ')).order_by('-start')
        else:
            if self.request.GET.get('speaker'):
                return self.model.objects.filter(sermons__isnull=False,
                                                 sermons__speakers=int(self.request.GET.get('speaker'))
                                                 ).order_by('-start')
            return self.model.objects.filter(sermons__isnull=False).order_by('-start')

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


class SermonsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'sermons.view_sermon'
    model = Sermon
    ordering = ('-event',)
    context_object_name = 'sermons'
    template_name = 'sermons/sermons-admin-list.html'
    page_title = 'Sermons - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('sermons:sermons-admin-create')


class SermonsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'sermons.add_sermon'
    model = Sermon
    template_name = 'admin-form-view.html'
    form_class = SermonCreateForm
    # fields = ('event', 'sermon_type', 'title', 'description', 'speakers', 'video_url', 'visible')
    success_url = reverse_lazy('sermons:sermons-admin-list')
    page_title = 'New Sermon - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('sermons:sermons-admin-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SermonAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'sermons.change_sermon'
    model = Sermon
    template_name = 'admin-form-view.html'
    form_class = SermonCreateForm
    success_url = reverse_lazy('sermons:sermons-admin-list')
    page_title = 'Update Sermon - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('sermons:sermons-admin-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
