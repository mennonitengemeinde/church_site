from django.urls import path

from core.views import HomeView
from core.views.pages import set_timezone

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('set_timezone/', set_timezone, name='set_timezone')
]
