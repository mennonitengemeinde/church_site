from django.urls import path

from songs.views import AdminChoirListView, AdminChoirCreateView

app_name = 'songs'

urlpatterns = [
    path('manage/choirs/', AdminChoirListView.as_view(), name='manage_choirs'),
    path('manage/choirs/create/', AdminChoirCreateView.as_view(), name='manage_choirs_create')
]