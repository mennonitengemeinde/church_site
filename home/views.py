from django.urls import reverse_lazy
from django.views.generic import CreateView

from contactus.forms import ContactUsForm
from schedules.selectors import get_events


class HomeView(CreateView):
    template_name = 'home/home.html'
    form_class = ContactUsForm
    page_title = 'Mennoniten Gemeinde'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = 'home'
        context['events'] = get_events(limit=12)
        return context

    def get_initial(self):
        initial = super(HomeView, self).get_initial()
        initial['page_title'] = self.page_title
        return initial
