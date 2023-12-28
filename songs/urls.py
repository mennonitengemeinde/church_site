from django.urls import path

from songs.views import AdminSongListView

app_name = 'songs'

urlpatterns = [
    path('manage/choirs/', AdminSongListView.as_view(), name='manage_choirs'),
    # path('manage/choirs/create/', AdminChoirCreateView.as_view(), name='manage_choirs_create')
]
