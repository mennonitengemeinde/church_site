from django.urls import path

from .apis import TelegramUserList, TelegramUserDetail

app_name = 'telegram-api'

urlpatterns = [
    path('users/', TelegramUserList.as_view()),
    path('users/<str:pk>/', TelegramUserDetail.as_view()),
]
