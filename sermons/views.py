from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from church_site.views import BaseListView, BaseDetailView, BaseCreateView, AdminListView, BaseUpdateView

from churches.models import Church
from sermons.forms import SermonCreateForm
from sermons.models import Sermon
from sermons.selectors import get_filtered_sermons, get_member_sermons
from speakers.models import Speaker


class SermonsListView(BaseListView):
    page_title = 'Sermons - Mennoniten Gemeinde'
    current_page = 'sermons'
    model = Sermon
    template_name = 'sermons/sermons-list.html'
    context_object_name = 'sermons'
    paginate_by = 18

    def get_queryset(self):
        return get_filtered_sermons(self.request.GET.get('church'), self.request.GET.get('speaker'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_church'] = self.request.GET.get('church') if self.request.GET.get('church') else None
        context['current_speaker'] = int(self.request.GET.get('speaker')) if self.request.GET.get('speaker') else None
        context['churches'] = Church.objects.all()
        context['speakers'] = Speaker.objects.all()
        context['page_filter'] = self.get_page_filter()
        return context

    def get_page_filter(self):
        """keeps the filter in get request when paginating"""
        if self.request_get.get('church') and self.request_get.get('speaker'):
            return f"church={self.request_get.get('church')}&speaker={self.request_get.get('speaker')}"
        elif self.request_get.get('church') and not self.request_get.get('speaker'):
            return f"church={self.request_get.get('church')}"
        elif self.request_get.get('speaker') and not self.request_get.get('church'):
            return f"speaker={self.request_get.get('speaker')}"


class SermonsDetailView(BaseDetailView):
    current_page = 'sermons'
    btn_back_href = reverse_lazy('sermons:sermons-list')
    model = Sermon
    template_name = 'sermons/sermons-detail.html'
    context_object_name = 'sermon'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        # Track views
        try:
            context['sermon'].views += 1
            context['sermon'].save()
        except Exception as e:
            print('Error', e)
        return context

    def get_page_title(self) -> str:
        return f'{self.object.event.start.strftime("%b %d, %Y")} - {self.object.title}'


class SermonsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'sermons.view_sermon'
    model = Sermon
    ordering = ('-event',)
    context_object_name = 'sermons'
    template_name = 'sermons/sermons-admin-list.html'
    page_title = 'Sermons - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('sermons:sermons-admin-create')
    paginate_by = 25

    def get_queryset(self):
        return get_member_sermons(self.request.user, reverse_order=True)


class SermonsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'sermons.add_sermon'
    model = Sermon
    template_name = 'sermons/sermons-admin-form.html'
    form_class = SermonCreateForm
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
    template_name = 'sermons/sermons-admin-form.html'
    form_class = SermonCreateForm
    success_url = reverse_lazy('sermons:sermons-admin-list')
    page_title = 'Update Sermon - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('sermons:sermons-admin-list')

    def get_queryset(self):
        return get_member_sermons(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
