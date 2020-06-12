from django.urls import path

from .views import (
    AttendantAdminDetailView,
    AttendantCreateView,
    AttendantAdminSignupToggle,
    EventsListView,
    EventsAdminListView,
    EventsAdminCreateView,
    EventsAdminUpdateView
)

app_name = 'schedules'

urlpatterns = [
    path('', EventsListView.as_view(), name='events-list'),
    path('<str:church>/', EventsListView.as_view(), name='events-list-filtered'),
    path('<str:church>/<int:event>/attendants/add', AttendantCreateView.as_view(), name='attendants-create'),
    path('manage/events/', EventsAdminListView.as_view(), name='events-admin-list'),
    path('manage/events/add/', EventsAdminCreateView.as_view(), name='events-admin-create'),
    path('manage/events/<int:pk>/update/', EventsAdminUpdateView.as_view(), name='events-admin-update'),
    path('manage/events/<int:pk>/attendants/', AttendantAdminDetailView.as_view(), name='attendants-admin-detail'),
    path('manage/events/<int:pk>/attendants/signup/toggle/', AttendantAdminSignupToggle.as_view(),
         name='attendants-admin-signup-toggle'),
]
