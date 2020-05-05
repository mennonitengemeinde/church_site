from django.views.generic import CreateView, DetailView, ListView, UpdateView


class PageProperties:
    page_title = None
    current_page = None


class BaseListView(PageProperties, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        return context


class BaseCreateView(PageProperties, CreateView):
    btn_back_href = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        context['btn_back_href'] = self.btn_back_href
        return context


class BaseDetailView(PageProperties, DetailView):
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_back_href'] = self.btn_back_href
        return context


class BaseUpdateView(PageProperties, UpdateView):
    btn_back_href = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = self.current_page
        context['btn_back_href'] = self.btn_back_href
        return context


class AdminListView(BaseListView):
    btn_add_href = None
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_add_href'] = self.btn_add_href
        return context
