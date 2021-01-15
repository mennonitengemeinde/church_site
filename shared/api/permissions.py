from django.conf import settings

from rest_framework.permissions import BasePermission


class ApiKeyAuthentication(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META.get('apikey')
        return api_key == settings.BOT_API_KEY
