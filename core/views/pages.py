import json

from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from contactus.forms import ContactUsForm
from core.views.base import BaseCreateView
from schedules.selectors import get_events
from sermons.selectors import get_random_sermons


class HomeView(BaseCreateView):
    template_name = 'core/home.html'
    form_class = ContactUsForm
    page_title = 'Mennoniten Gemeinde'
    current_page = 'home'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


@csrf_exempt
@require_http_methods(["POST"])
def set_timezone(request):
    data = json.loads(request.body)
    active_timezone = timezone.get_current_timezone()
    server_timezone = settings.TIME_ZONE
    if active_timezone == data["timezone"]:
        return JsonResponse({"success": True, "redirect": False}, status=200)
    
    request.session["user_timezone"] = data["timezone"]
    if server_timezone == data["timezone"] and active_timezone == data["timezone"]:
        return JsonResponse({"success": True, "reload": False}, status=200)
    return JsonResponse({"success": True, "reload": True}, status=200)
