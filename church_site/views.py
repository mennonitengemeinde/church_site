from typing import List

from django.core.paginator import Page
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class PageProperties:
    page_title = None
    current_page = None


class FormProperties:
    form_has_files = False


class BaseListView(PageProperties, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        if context['page_obj']:
            context['pagination_links'] = self.get_pagination_links(context['page_obj'])
        return context

    @staticmethod
    def get_pagination_links(page: Page) -> List[int]:
        """returns pagination links for paginated lists"""
        if page.paginator.num_pages > 5:
            links = []
            for p in page.paginator.page_range:
                if 5 >= p > 3 > page.number:
                    links.append(p)
                elif p > page.paginator.count - 5 and page.number > page.paginator.count - 3:
                    links.append(p)
                elif (page.number + 2) >= p >= (page.number - 2):
                    links.append(p)
            return links
        else:
            return page.paginator.page_range


class BaseCreateView(PageProperties, FormProperties, CreateView):
    btn_back_href = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        context['btn_back_href'] = self.btn_back_href
        context['form_has_files'] = self.form_has_files
        return context


class BaseDetailView(PageProperties, DetailView):
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_back_href'] = self.btn_back_href
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        return context


class BaseUpdateView(PageProperties, FormProperties, UpdateView):
    btn_back_href = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        context['btn_back_href'] = self.btn_back_href
        context['form_has_files'] = self.form_has_files
        return context


class AdminListView(BaseListView):
    btn_add_href = None
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_add_href'] = self.btn_add_href
        context['btn_back_href'] = self.btn_back_href
        return context
