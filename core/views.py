from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView

from contactus.forms import ContactUsForm
from schedules.selectors import get_events
from sermons.selectors import get_random_sermons


class CoreView(View):
    template_name: str = None
    current_page: str = None
    btn_back_href: str = None
    btn_add_href: str = None

    def get_template_name(self):
        return self.template_name

    def get_current_page(self):
        return self.current_page

    def get_btn_back_href(self):
        return self.btn_back_href

    def get_btn_add_href(self):
        return self.btn_add_href

    def get_context_data(self, **kwargs):
        context = {
            'template_name': self.get_template_name(),
            'current_page': self.get_current_page(),
            'btn_back_href': self.get_btn_back_href(),
            'btn_add_href': self.get_btn_add_href(),
        }
        return context


class HomeView(CreateView):
    template_name = 'core/home.html'
    form_class = ContactUsForm
    page_title = 'Mennoniten Gemeinde'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['current_page'] = 'home'
        events = get_events(limit=5)
        local_timezone = timezone.get_current_timezone()
        for event in events:
            event.start = event.start.astimezone(local_timezone)
        context['events'] = events
        context['sermons'] = get_random_sermons(limit=5)
        return context

    def get_initial(self):
        initial = super(HomeView, self).get_initial()
        initial['page_title'] = self.page_title
        return initial
