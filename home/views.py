from django.views.generic import TemplateView

from contactus.forms import ContactUsForm
from schedules.models import Event


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Mennoniten Gemeinde'
        context['current_page'] = 'home'
        context['events'] = Event.objects.get_first_twelve()
        context['contact_form'] = ContactUsForm
        return context
