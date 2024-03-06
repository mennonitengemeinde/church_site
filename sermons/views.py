import logging
from typing import List

from churches.models import Church
from core.views.base import (
    AdminListView,
    BaseCreateView,
    BaseDetailView,
    BaseListView,
    BaseUpdateView,
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from speakers.models import Speaker

from sermons.forms import SermonCreateForm
from sermons.models import Sermon
from sermons.selectors import (
    get_member_sermons,
    get_filtered_sermon_list,
)

logger = logging.getLogger(__name__)


class SermonsListView(BaseListView):
    page_title = "Sermons - Mennoniten Gemeinde"
    current_page = "sermons"
    model = Sermon
    template_name = "sermons/sermon-list.html"
    context_object_name = "sermons"
    paginate_by = 18

    def get(self, request, *args, **kwargs):
        res = super().get(request, *args, **kwargs)
        if (
            request.GET.get("church")
            or request.GET.get("drop-church")
            or request.GET.get("speaker")
            or request.GET.get("drop-speaker")
        ):
            if self.get_query_url():
                res["HX-Push-Url"] = f"?{self.get_query_url()}"
            else:
                res["HX-Push-Url"] = "/"
        return res

    def get_queryset(self):
        filter_churches_q = self.serialize_filter_query(
            "churches", "church", "drop-church"
        )
        filter_speakers_q = self.serialize_filter_query(
            "speakers", "speaker", "drop-speaker"
        )
        return get_filtered_sermon_list(filter_churches_q, filter_speakers_q)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["churches"] = Church.objects.all()
        context["speakers"] = Speaker.objects.all()
        context["page_filter"] = self.get_query_url()
        context["active_church_filter"] = context["churches"].filter(
            id__in=self.serialize_filter_query("churches", "church", "drop-church")
        )
        context["active_speaker_filter"] = context["speakers"].filter(
            id__in=self.serialize_filter_query("speakers", "speaker", "drop-speaker")
        )
        return context

    def serialize_filter_query(
        self, active_list_key: str, add_filter_key: str, drop_filter_key: str
    ) -> List[int]:
        data: List[int] = []
        if self.request.GET.get(active_list_key):
            data = self.request.GET.get(active_list_key).split(",")
            data = [int(d) for d in data]
        if self.request.GET.get(add_filter_key):
            data.append(int(self.request.GET.get(add_filter_key)))
        if self.request.GET.get(drop_filter_key):
            data.remove(int(self.request.GET.get(drop_filter_key)))
        return data

    def get_query_url(self) -> str | None:
        churches = self.serialize_filter_query("churches", "church", "drop-church")
        speakers = self.serialize_filter_query("speakers", "speaker", "drop-speaker")

        if churches and speakers:
            return f"churches={','.join(str(x) for x in churches)}&speakers={','.join(str(x) for x in speakers)}"
        if churches and not speakers:
            return f"churches={','.join(str(x) for x in churches)}"
        if speakers and not churches:
            return f"speakers={','.join(str(x) for x in speakers)}"
        return None

    #
    # def get_request_filter(self, key: str) -> List[int]:
    #     data = []
    #     if self.request.GET.get(key) and self.request.GET.get(key) != [""]:
    #         data = self.request.GET.get(key).split(",")
    #         data = [int(d) for d in data]
    #     return data
    #
    # def get_filter_list(self, filter_list: str, filter_key: str) -> list[int]:
    #     f_list = self.get_request_filter(filter_list)
    #     if self.request.GET.get(filter_key):
    #         f_list.append(int(self.request.GET.get(filter_key)))
    #     return f_list
    #
    # def get_filter_list_string(self, filter_list: str, filter_key: str) -> str:
    #     f_list = self.get_filter_list(filter_list, filter_key)
    #     return ",".join(str(x) for x in f_list)
    #
    # def get_page_filter(self) -> str | None:
    #     """keeps the filter in get request when paginating"""
    #     if self.request.GET.get("churches") and self.request.GET.get("speakers"):
    #         return f"churches={self.request.GET.get('churches')}&speakers={self.request.GET.get('speakers')}"
    #     elif self.request.GET.get("churches") and not self.request.GET.get("speakers"):
    #         return f"churches={self.request.GET.get('churches')}"
    #     elif self.request.GET.get("speakers") and not self.request.GET.get("churches"):
    #         return f"speakers={self.request.GET.get('speakers')}"
    #     return None


class SermonsDetailView(BaseDetailView):
    current_page = "sermons"
    btn_back_href = reverse_lazy("sermons:sermons-list")
    model = Sermon
    template_name = "sermons/sermon-detail.html"
    context_object_name = "sermon"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()
        # Track views
        try:
            context["sermon"].views += 1
            context["sermon"].save()
        except Exception as e:
            logger.error(e)
        return context

    def get_page_title(self) -> str:
        return f'{self.object.event.start.strftime("%b %d, %Y")} - {self.object.title}'


class SermonsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = "sermons.view_sermon"
    model = Sermon
    ordering = ("-event",)
    context_object_name = "sermons"
    template_name = "sermons/sermons-admin-list.html"
    page_title = "Sermons - Admin"
    current_page = "admin_sermons"
    btn_add_href = reverse_lazy("sermons:sermons-admin-create")
    paginate_by = 25

    def get_template_names(self):
        if self.request.htmx:
            return "sermons/partials/sermon-admin-list-partial.html"
        else:
            return self.template_name

    def get_queryset(self):
        return get_member_sermons(self.request.user, reverse_order=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pagination_links'] = self.get_pagination_links(context['page_obj'])
        return context


class SermonsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = "sermons.add_sermon"
    model = Sermon
    template_name = "admin-form-view.html"
    form_class = SermonCreateForm
    success_url = reverse_lazy("sermons:sermons-admin-list")
    page_title = "New Sermon - Admin"
    current_page = "admin_sermons"
    btn_back_href = reverse_lazy("sermons:sermons-admin-list")
    form_has_files = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class SermonAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = "sermons.change_sermon"
    model = Sermon
    template_name = "admin-form-view.html"
    form_class = SermonCreateForm
    success_url = reverse_lazy("sermons:sermons-admin-list")
    page_title = "Update Sermon - Admin"
    current_page = "admin_sermons"
    btn_back_href = reverse_lazy("sermons:sermons-admin-list")
    form_has_files = True

    def get_queryset(self):
        return get_member_sermons(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


def download_sermon(request, pk):
    sermon = Sermon.objects.filter(id=pk).first()
    if sermon:
        response = HttpResponse(sermon.audio_low, content_type="audio/mpeg")
        response["Content-Disposition"] = f"attachment; filename={sermon.title}.mp3"
        return response
    else:
        raise Http404("Sermon not found")
