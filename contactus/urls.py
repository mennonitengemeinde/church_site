from django.urls import path

from .views import AdminContactMessageListView, AdminContactMessageDetailView, AdminReadMessage, AdminContactMessageDeleteView

app_name = 'contactus'

urlpatterns = [
    path('manage/messages/', AdminContactMessageListView.as_view(), name='admin-messages'),
    path('manage/messages/<int:pk>/', AdminContactMessageDetailView.as_view(), name='admin-message-detail'),
    path('manage/messages/<int:pk>/read/', AdminReadMessage.as_view(), name='admin-read-message'),
    path('manage/messages/<int:pk>/delete/', AdminContactMessageDeleteView.as_view(), name='admin-delete-message'),
]
