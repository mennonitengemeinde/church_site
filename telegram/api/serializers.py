from rest_framework import serializers

from telegram.models import LiveSubscription


class LiveSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveSubscription
        fields = ['id', 'chat_type', 'name', 'language_code']