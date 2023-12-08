from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from core.views.base import BaseCreateView, AdminListView
from songs.forms import ChoirCreateForm
from songs.models import Choir


class AdminChoirListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'songs.view_choir'
    model = Choir
    context_object_name = 'choirs'
    page_title = 'Choirs - Admin'
    current_page = 'admin_choirs'
    btn_add_href = reverse_lazy('songs:manage_choirs_create')
    template_name = 'songs/manage/choir-list.html'


class AdminChoirCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'songs.add_choir'
    model = Choir
    template_name = 'admin-form-view.html'
    form_class = ChoirCreateForm
    page_title = 'New Choir - Admin'
    current_page = 'admin_choirs'
    btn_back_href = '/admin/choirs/'
    success_url = reverse_lazy('songs:manage_choirs')
