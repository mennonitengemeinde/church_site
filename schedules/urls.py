from django.urls import path

from .views import EventsListView

app_name = 'schedules'

urlpatterns = [
    path('', EventsListView.as_view(), name='events-list'),
    path('<str:church>/', EventsListView.as_view(), name='events-list-filtered'),
]
