from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

from church_site.views import AdminListView, BaseCreateView, BaseUpdateView
from .forms import SpeakerCreateForm

from .models import Speaker


class SpeakersAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'speakers.view_speaker'
    model = Speaker
    template_name = 'speakers/speakers-admin-list.html'
    context_object_name = 'speakers'
    page_title = 'Speakers - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('speakers:speakers-admin-create')
    

class SpeakersAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'speakers.add_speaker'
    model = Speaker
    template_name = 'admin-form-view.html'
    form_class = SpeakerCreateForm
    page_title = 'New Speaker - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('speakers:speakers-admin-list')
    success_url = reverse_lazy('speakers:speakers-admin-list')


class SpeakerAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'speakers.change_speaker'
    model = Speaker
    template_name = 'admin-form-view.html'
    form_class = SpeakerCreateForm
    page_title = 'Update Speaker - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('speakers:speakers-admin-list')
    success_url = reverse_lazy('speakers:speakers-admin-list')
