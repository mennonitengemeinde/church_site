from django.urls import reverse_lazy

from church_site.views import AdminListView, BaseCreateView

from churches.models import Church


class ChurchesAdminListView(AdminListView):
    page_title = 'Churches - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('churches-admin-create')
    model = Church
    context_object_name = 'churches'
    template_name = 'churches/churches-admin-list.html'


class ChurchesAdminCreateView(BaseCreateView):
    page_title = 'Create Church - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('churches-admin-list')
    model = Church
    template_name = 'churches/churches-admin-form.html'
    fields = ('name', 'street', 'city', 'province_state', 'country', 'mixlr_url')
