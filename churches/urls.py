from django.urls import path

from .views import ChurchesAdminListView, ChurchesAdminCreateView

urlpatterns = [
    path('manage/churches/', ChurchesAdminListView.as_view(), name='churches-admin-list'),
    path('manage/churches/add/', ChurchesAdminCreateView.as_view(), name='churches-admin-create'),
]
