from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from church_site.views import AdminListView, BaseCreateView, BaseUpdateView
from churches.forms import ChurchCreateForm

from churches.models import Church
from churches.selectors import get_member_churches


class ChurchesAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'churches.view_church'
    page_title = 'Churches - Admin'
    current_page = 'admin_churches'
    btn_add_href = reverse_lazy('churches:churches-admin-create')
    model = Church
    context_object_name = 'churches'
    template_name = 'churches/churches-admin-list.html'


class ChurchesAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'churches.add_church'
    page_title = 'New Church - Admin'
    current_page = 'admin_churches'
    btn_back_href = reverse_lazy('churches:churches-admin-list')
    model = Church
    template_name = 'admin-form-view.html'
    form_class = ChurchCreateForm
    success_url = reverse_lazy('churches:churches-admin-list')


class ChurchesAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'churches.change_church'
    page_title = 'Update Church - Admin'
    current_page = 'admin_churches'
    btn_back_href = reverse_lazy('churches:churches-admin-list')
    model = Church
    template_name = 'admin-form-view.html'
    form_class = ChurchCreateForm
    success_url = reverse_lazy('churches:churches-admin-list')

    def get_queryset(self):
        return get_member_churches(user=self.request.user)
