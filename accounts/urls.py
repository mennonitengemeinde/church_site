from django.urls import path

from accounts.views import UsersAdminListView, UsersAdminUpdateView

app_name = 'accounts'

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('manage/users/', UsersAdminListView.as_view(), name='users-admin-list'),
    path('manage/users/<int:pk>/update', UsersAdminUpdateView.as_view(), name='users-admin-update'),
]
