from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from accounts.forms import UpdateUserForm
from church_site.views import AdminListView, BaseUpdateView


class UsersAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'accounts.view_user'
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'accounts/users-admin-list.html'
    page_title = 'Users - Admin'
    current_page = 'manage'


class UsersAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'accounts.change_user'
    model = get_user_model()
    template_name = 'admin-form-view.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('accounts:users-admin-list')
    page_title = 'Update User - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('accounts:users-admin-list')
