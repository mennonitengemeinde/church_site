from django.conf import settings

from rest_framework.permissions import BasePermission


class ApiKeyAuthentication(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('apikey')
        # api_key = request.META.get('apikey')
        print(api_key)
        print(settings.BOT_API_KEY)
        return api_key == settings.BOT_API_KEY
