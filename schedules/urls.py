from django.urls import path

from .views import EventsListView, EventsAdminListView, EventsAdminCreateView, EventsAdminUpdateView

app_name = 'schedules'

urlpatterns = [
    path('', EventsListView.as_view(), name='events-list'),
    path('<str:church>/', EventsListView.as_view(), name='events-list-filtered'),
    path('manage/events/', EventsAdminListView.as_view(), name='events-admin-list'),
    path('manage/events/add/', EventsAdminCreateView.as_view(), name='events-admin-create'),
    path('manage/events/<int:pk>/update/', EventsAdminUpdateView.as_view(), name='events-admin-update'),
]
