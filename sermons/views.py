from church_site.views import BaseListView

from .models import Sermon


class SermonsListView(BaseListView):
    page_title = 'Sermons'
    current_page = 'sermons'
    model = Sermon
    template_name = 'sermons/sermons-list.html'
    context_object_name = 'sermons'
