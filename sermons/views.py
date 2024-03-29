import logging
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Page
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy

from church_site.views import BaseListView, BaseDetailView, BaseCreateView, AdminListView, BaseUpdateView
from churches.models import Church
from sermons.forms import SermonCreateForm
from sermons.models import Sermon
from sermons.selectors import get_filtered_sermons, get_member_sermons
from speakers.models import Speaker

logger = logging.getLogger(__name__)


class SermonsListView(BaseListView):
    page_title = 'Sermons - Mennoniten Gemeinde'
    current_page = 'sermons'
    model = Sermon
    template_name = 'sermons/sermon-list.html'
    context_object_name = 'sermons'
    paginate_by = 18

    def get_queryset(self):
        return get_filtered_sermons(
            church=self.request.GET.get('church') if self.request.GET.get('church') != 'all' else None,
            speaker=self.request.GET.get('speaker') if self.request.GET.get('speaker') != 'all' else None
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_church'] = self.request.GET.get('church') if self.request.GET.get('church') != 'all' else None
        if self.request.GET.get('speaker') and self.request.GET.get('speaker') != 'all':
            context['current_speaker'] = int(self.request.GET.get('speaker'))
        else:
            context['current_speaker'] = None
        context['churches'] = Church.objects.all()
        context['speakers'] = Speaker.objects.all()
        context['page_filter'] = self.get_page_filter()
        # context['pagination_links'] = self.get_pagination_links(context['page_obj'])
        if self.request.htmx:
            self.template_name = 'sermons/partials/sermon-list-partial.html'
        return context

    def get_page_filter(self):
        """keeps the filter in get request when paginating"""
        if self.request.GET.get('church') and self.request.GET.get('speaker'):
            return f"church={self.request.GET.get('church')}&speaker={self.request.GET.get('speaker')}"
        elif self.request.GET.get('church') and not self.request.GET.get('speaker'):
            return f"church={self.request.GET.get('church')}"
        elif self.request.GET.get('speaker') and not self.request.GET.get('church'):
            return f"speaker={self.request.GET.get('speaker')}"

    # @staticmethod
    # def get_pagination_links(page: Page):
    #     """returns pagination links for the sermons list"""
    #     if page.paginator.num_pages > 5:
    #         links = []
    #         for p in page.paginator.page_range:
    #             if 5 >= p > 3 > page.number:
    #                 links.append(p)
    #             elif p > page.paginator.count - 5 and page.number > page.paginator.count - 3:
    #                 links.append(p)
    #             elif (page.number + 2) >= p >= (page.number - 2):
    #                 links.append(p)
    #         return links
    #     else:
    #         return page.paginator.page_range


class SermonsDetailView(BaseDetailView):
    current_page = 'sermons'
    btn_back_href = reverse_lazy('sermons:sermons-list')
    model = Sermon
    template_name = 'sermons/sermon-detail.html'
    context_object_name = 'sermon'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        # Track views
        try:
            context['sermon'].views += 1
            context['sermon'].save()
        except Exception as e:
            logger.error(e)
        return context

    def get_page_title(self) -> str:
        return f'{self.object.event.start.strftime("%b %d, %Y")} - {self.object.title}'


class SermonsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'sermons.view_sermon'
    model = Sermon
    ordering = ('-event',)
    context_object_name = 'sermons'
    template_name = 'sermons/sermons-admin-list.html'
    page_title = 'Sermons - Admin'
    current_page = 'admin_sermons'
    btn_add_href = reverse_lazy('sermons:sermons-admin-create')
    paginate_by = 25

    def get_template_names(self):
        if self.request.htmx:
            return 'sermons/partials/sermon-admin-list-partial.html'
        else:
            return self.template_name

    def get_queryset(self):
        return get_member_sermons(self.request.user, reverse_order=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pagination_links'] = self.get_pagination_links(context['page_obj'])
        return context


class SermonsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'sermons.add_sermon'
    model = Sermon
    template_name = 'admin-form-view.html'
    form_class = SermonCreateForm
    success_url = reverse_lazy('sermons:sermons-admin-list')
    page_title = 'New Sermon - Admin'
    current_page = 'admin_sermons'
    btn_back_href = reverse_lazy('sermons:sermons-admin-list')
    form_has_files = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SermonAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'sermons.change_sermon'
    model = Sermon
    template_name = 'admin-form-view.html'
    form_class = SermonCreateForm
    success_url = reverse_lazy('sermons:sermons-admin-list')
    page_title = 'Update Sermon - Admin'
    current_page = 'admin_sermons'
    btn_back_href = reverse_lazy('sermons:sermons-admin-list')
    form_has_files = True

    def get_queryset(self):
        return get_member_sermons(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def download_sermon(request, pk):
    sermon = Sermon.objects.filter(id=pk).first()
    if sermon:
        response = HttpResponse(sermon.audio_low, content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename={sermon.title}.mp3'
        return response
    else:
        raise Http404('Sermon not found')
