from django.urls import path

from .views import (StreamsListView, LiveAudioView, LiveVideoView, StreamsAdminListView, StreamsAdminCreateView,
                    StreamAdminUpdateView, StreamAdminLiveUpdateView)

app_name = 'streams'

urlpatterns = [
    path('live/', StreamsListView.as_view(), name='streams-list'),
    path('live/<str:church>/', StreamsListView.as_view(), name='streams-list-filtered'),
    path('live/<str:church>/<int:pk>/audio/', LiveAudioView.as_view(), name='live-audio'),
    path('live/<str:church>/<int:pk>/video/', LiveVideoView.as_view(), name='live-video'),
    path('manage/streams/', StreamsAdminListView.as_view(), name='streams-admin-list'),
    path('manage/streams/add/', StreamsAdminCreateView.as_view(), name='streams-admin-create'),
    path('manage/streams/<int:pk>/update/', StreamAdminUpdateView.as_view(), name='streams-admin-update'),
    path('manage/streams/<int:pk>/live/', StreamAdminLiveUpdateView.as_view(), name='streams-admin-update-live'),
]
