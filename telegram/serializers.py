from rest_framework import serializers

from telegram.models import TelegramUser


class TelegramUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['first_name', 'last_name', 'chat_id', 'preferred_language', 'bot']


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id', 'first_name', 'last_name', 'chat_id', 'preferred_language', 'bot']
