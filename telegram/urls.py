from django.conf import settings
from django.urls import path

# from .views import webhook

app_name = 'telegram'

urlpatterns = [
    # path(f'webhook/{settings.WOL_EVENTS_BOT_TOKEN}/', webhook, name='telegram-webhook'),
]
