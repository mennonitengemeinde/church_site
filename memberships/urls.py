from django.urls import path

from memberships.views import FamilyAdminCreateView, FamilyAdminDetailView, FamilyAdminListView

app_name = 'memberships'

urlpatterns = [
    path('manage/families/', FamilyAdminListView.as_view(), name='families-admin-list'),
    path('manage/families/add/', FamilyAdminCreateView.as_view(), name='families-admin-create'),
    path('manage/families/<int:pk>/', FamilyAdminDetailView.as_view(), name='families-admin-detail'),
]
