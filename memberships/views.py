from django.urls import reverse_lazy

from church_site.views import BaseListView, AdminListView, BaseCreateView, BaseDetailView
from memberships.forms import FamilyForm
from memberships.models import Family


class FamilyAdminCreateView(BaseCreateView):
    template_name = 'admin-form-view.html'
    model = Family
    form_class = FamilyForm
    page_title = 'New Family - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('memberships:families-admin-list')
    success_url = reverse_lazy('memberships:families-admin-list')


class FamilyAdminDetailView(BaseDetailView):
    template_name = 'memberships/families-admin-detail.html'
    model = Family
    context_object_name = 'family'
    page_title = 'Family - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('memberships:families-admin-list')

    def get_context_data(self, **kwargs):
        context = super(FamilyAdminDetailView, self).get_context_data(**kwargs)
        context['father'] = self.object.parents.filter(parent_type=1).first()
        context['mother'] = self.object.parents.filter(parent_type=2).first()
        return context


class FamilyAdminListView(AdminListView):
    template_name = 'memberships/families-admin-list.html'
    model = Family
    context_object_name = 'families'
    page_title = 'Families - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('memberships:families-admin-create')
