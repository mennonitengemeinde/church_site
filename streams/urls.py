from django.urls import path

from .views import StreamsListView

app_name = 'streams'

urlpatterns = [
    path('live/', StreamsListView.as_view(), name='streams-list'),
]
