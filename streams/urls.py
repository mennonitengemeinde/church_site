from django.urls import path

from .views import StreamsListView, LiveAudioView, LiveVideoView

app_name = 'streams'

urlpatterns = [
    path('live/', StreamsListView.as_view(), name='streams-list'),
    path('live/<str:church>/<int:pk>/audio', LiveAudioView.as_view(), name='live-audio'),
    path('live/<str:church>/<int:pk>/video', LiveVideoView.as_view(), name='live-video'),
]
