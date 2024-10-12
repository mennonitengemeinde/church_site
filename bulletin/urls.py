from django.urls import path

from bulletin.views import BulletinAdminCreateView, BulletinAdminDetailView, BulletinAdminListView

app_name = 'bulletin'

urlpatterns = [
    path('manage/bulletins/', BulletinAdminListView.as_view(), name='bulletins-admin-list'),
    path('manage/bulletins/add/', BulletinAdminCreateView.as_view(), name='bulletins-admin-create'),
    path('manage/bulletins/<int:pk>/', BulletinAdminDetailView.as_view(), name='bulletins-admin-detail'),
]
