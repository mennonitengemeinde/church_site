from django.utils import timezone

from church_site.views import BaseListView

from .models import Stream


class StreamsListView(BaseListView):
    page_title = 'Live'
    current_page = 'live'
    model = Stream
    template_name = 'streams/streams-list.html'
    context_object_name = 'streams'

    def get_queryset(self):
        return Stream.objects.filter(event__end__gt=timezone.now())
