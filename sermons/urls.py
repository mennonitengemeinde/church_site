from django.urls import path

from .views import (
    SermonsListView,
    SermonsDetailView,
    SermonsAdminCreateView,
    SermonsAdminListView,
)

app_name = 'sermons'

urlpatterns = [
    path('', SermonsListView.as_view(), name='sermons-list'),
    path('<str:church>/', SermonsListView.as_view(), name='sermons-list-filtered'),
    path('<str:church>/<int:pk>/', SermonsDetailView.as_view(), name='sermons-detail'),
    path('manage/sermons/', SermonsAdminListView.as_view(), name='sermons-admin-list'),
    path('manage/sermons/add/', SermonsAdminCreateView.as_view(), name='sermons-admin-create'),
]
