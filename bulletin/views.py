from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from bulletin.forms import BulletinCreateForm
from bulletin.models import Bulletin
from core.views.base import AdminListView, BaseCreateView, BaseDetailView


class BulletinAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'bulletin.view_bulletin'
    page_title = 'Bulletins - Admin'
    current_page = 'admin_bulletin'
    btn_add_href = reverse_lazy('bulletin:bulletins-admin-create')
    model = Bulletin
    context_object_name = 'bulletins'
    template_name = 'bulletin/bulletin-admin-list.html'


class BulletinAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'bulletin.add_bulletin'
    page_title = 'New Bulletin - Admin'
    current_page = 'admin_bulletin'
    btn_back_href = reverse_lazy('bulletin:bulletins-admin-list')
    model = Bulletin
    template_name = 'admin-form-view.html'
    form_class = BulletinCreateForm
    success_url = reverse_lazy('bulletin:bulletins-admin-list')


class BulletinAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'bulletin.view_bulletin'
    page_title = 'Bulletin - Admin'
    current_page = 'admin_bulletin'
    btn_back_href = reverse_lazy('bulletin:bulletins-admin-list')
    model = Bulletin
    template_name = 'bulletin/bulletin-admin-detail.html'
    context_object_name = 'bulletin'
