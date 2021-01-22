from rest_framework import serializers

from telegram.models import LiveSubscription


class SubscriptionDetailSerializer(serializers.Serializer):
    live = serializers.BooleanField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class LiveSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveSubscription
        fields = ['id', 'chat_id', 'chat_type', 'name', 'language_code']
