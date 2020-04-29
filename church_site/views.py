from django.views.generic import ListView


class AdminListView(ListView):
    btn_add_href = None
    btn_back_href = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_add_href'] = self.btn_add_href
        context['btn_back_href'] = self.btn_back_href
        return context
