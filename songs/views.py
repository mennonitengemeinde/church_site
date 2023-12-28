from core.views.base import BaseListView
from songs.models import Song


class AdminSongListView(BaseListView):
    model = Song
    template_name = 'songs/manage/choir-list.html'
    context_object_name = 'songs'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return Song.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminSongListView, self).get_context_data(**kwargs)
        context['title'] = 'Admin Song List'
        return context
