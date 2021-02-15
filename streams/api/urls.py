from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from streams.api.controllers import StreamsList

urlpatterns = [
    path('', StreamsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
