from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

from accounts.forms import UpdateUserForm
from accounts.models import User
from church_site.views import AdminListView, BaseUpdateView


class UsersAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'accounts.view_user'
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'accounts/users-admin-list.html'
    page_title = 'Users - Admin'
    current_page = 'manage'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(Q(member__in=self.request.user.churches.all()) | Q(member__isnull=True)).distinct()


class UsersAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'accounts.change_user'
    model = get_user_model()
    template_name = 'admin-form-view.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('accounts:users-admin-list')
    page_title = 'Update User - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('accounts:users-admin-list')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(Q(member__in=self.request.user.churches.all()) | Q(member__isnull=True)).distinct()

