from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from churches.forms import ChurchCreateForm, ChoirCreateForm
from churches.models import Church, Choir
from churches.selectors import get_member_churches
from core.views.base import (
    AdminListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
)


class ChurchesAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = "churches.view_church"
    page_title = "Churches - Admin"
    current_page = "admin_churches"
    btn_add_href = reverse_lazy("churches:churches-admin-create")
    model = Church
    context_object_name = "churches"
    template_name = "churches/manage/churches-admin-list.html"


class ChurchesAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = "churches.view_church"
    page_title = "Church - Admin"
    current_page = "admin_churches"
    btn_back_href = reverse_lazy("churches:churches-admin-list")
    model = Church
    template_name = "churches/manage/church-details.html"
    context_object_name = "church"

    def get_queryset(self):
        return get_member_churches(user=self.request.user)


class ChurchesAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = "churches.add_church"
    page_title = "New Church - Admin"
    current_page = "admin_churches"
    btn_back_href = reverse_lazy("churches:churches-admin-list")
    model = Church
    template_name = "admin-form-view.html"
    form_class = ChurchCreateForm
    success_url = reverse_lazy("churches:churches-admin-list")


class ChurchesAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = "churches.change_church"
    page_title = "Update Church - Admin"
    current_page = "admin_churches"
    btn_back_href = reverse_lazy("churches:churches-admin-list")
    model = Church
    template_name = "admin-form-view.html"
    form_class = ChurchCreateForm
    success_url = reverse_lazy("churches:churches-admin-list")

    def get_queryset(self):
        return get_member_churches(user=self.request.user)


class AdminChoirCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = "songs.add_choir"
    model = Choir
    template_name = "admin-form-view.html"
    form_class = ChoirCreateForm
    page_title = "New Choir - Admin"
    current_page = "admin_choirs"
    btn_back_href = reverse_lazy("churches:churches-admin-list")
    success_url = reverse_lazy("churches:churches-admin-list")

    def get_initial(self):
        initial = super().get_initial()
        initial["church"] = self.kwargs["pk"]
        return initial

    def get_btn_back_href(self):
        return reverse_lazy(
            "churches:churches-admin-detail", kwargs={"pk": self.kwargs["pk"]}
        )

    def get_success_url(self):
        return reverse_lazy(
            "churches:churches-admin-detail", kwargs={"pk": self.kwargs["pk"]}
        )
