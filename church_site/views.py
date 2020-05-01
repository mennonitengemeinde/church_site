from django.views.generic import ListView, CreateView


class BaseListView(ListView):
    page_title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class BaseCreateView(CreateView):
    page_title = None
    btn_back_href = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['btn_back_href'] = self.btn_back_href
        return context


class AdminListView(BaseListView):
    btn_add_href = None
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_add_href'] = self.btn_add_href
        return context
