from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from telegram.models import TelegramUser
from telegram.serializers import TelegramUserCreateSerializer, TelegramUserSerializer


class TelegramUserList(APIView):
    """
    Create a new Telegram User.
    """
    def post(self, request, format=None):
        serializer = TelegramUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TelegramUserDetail(APIView):
    """
    Retrieve, update or delete a Telegram User instance.
    """
    def get_object(self, pk):
        try:
            return TelegramUser.objects.get(chat_id=pk)
        except TelegramUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        t_user = self.get_object(pk)
        serializer = TelegramUserSerializer(t_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        t_user = self.get_object(pk)
        serializer = TelegramUserSerializer(t_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        t_user = self.get_object(pk)
        t_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
