from rest_framework import viewsets

from telegram.api.serializers import LiveSubscriptionSerializer
from telegram.models import LiveSubscription

from shared.api.permissions import ApiKeyAuthentication


class LiveSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = LiveSubscription.objects.all()
    serializer_class = LiveSubscriptionSerializer
    permission_classes = [ApiKeyAuthentication]
