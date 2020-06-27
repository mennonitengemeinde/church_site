from django.urls import path

from .views import (
    EventsAdminDetailView,
    AttendantCreateView,
    AttendantAdminDetailView,
    AttendantAdminDeleteView,
    AttendantAdminUpdateView,
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
    path('manage/events/<int:pk>/', EventsAdminDetailView.as_view(), name='events-admin-detail'),
    path('manage/events/<int:event>/attendants/<int:pk>/', AttendantAdminDetailView.as_view(),
         name='attendants-admin-detail'),
    path('manage/events/<int:event>/attendants/<int:pk>/update/', AttendantAdminUpdateView.as_view(),
         name='attendants-admin-update'),
    path('manage/events/<int:event>/attendants/<int:pk>/delete/', AttendantAdminDeleteView.as_view(),
         name='attendants-admin-delete'),
    path('manage/events/<int:pk>/attendants/signup/toggle/', AttendantAdminSignupToggle.as_view(),
         name='attendants-admin-signup-toggle'),
]
