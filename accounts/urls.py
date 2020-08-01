from django.urls import path

from accounts.views import (
    GroupsAdminCreateView,
    GroupsAdminListView,
    GroupsAdminUpdateView,
    UsersAdminListView,
    UsersAdminUpdateView,
    UserProfileView
)

app_name = 'accounts'

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('manage/users/', UsersAdminListView.as_view(), name='users-admin-list'),
    path('manage/users/<int:pk>/update', UsersAdminUpdateView.as_view(), name='users-admin-update'),
    path('manage/groups/', GroupsAdminListView.as_view(), name='groups-admin-list'),
    path('manage/groups/add', GroupsAdminCreateView.as_view(), name='groups-admin-create'),
    path('manage/groups/<int:pk>/update', GroupsAdminUpdateView.as_view(), name='groups-admin-update'),
]
