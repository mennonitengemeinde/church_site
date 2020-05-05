from django.urls import path

from .views import SermonsListView, SermonsDetailView

app_name = 'sermons'

urlpatterns = [
    path('', SermonsListView.as_view(), name='sermons-list'),
    path('<int:pk>/', SermonsDetailView.as_view(), name='sermons-detail'),
]
