from django.urls import path

from .views import SpeakersAdminListView, SpeakersAdminCreateView

app_name = 'speakers'

urlpatterns = [
    path('manage/speakers', SpeakersAdminListView.as_view(), name='speakers-admin-list'),
    path('manage/speakers/add', SpeakersAdminCreateView.as_view(), name='speakers-admin-create'),
]
