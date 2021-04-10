# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import GenericViewSet, mixins
#
# from telegram.api.serializers import LiveSubscriptionSerializer, SubscriptionDetailSerializer
# from telegram.models import LiveSubscription
#
# from accounts.permissions import ApiKeyAuthentication
#
#
# class SubscriptionDetail(APIView):
#     permission_classes = [ApiKeyAuthentication]
#
#     def get(self, request, pk):
#         print('running get')
#         sub = LiveSubscription.objects.filter(chat_id=pk).first()
#         print(sub)
#         data = {'live': False}
#         if sub:
#             data['live'] = True
#
#         serializer = SubscriptionDetailSerializer(data)
#
#         return Response(serializer.data)
#
#
# class LiveSubscriptionViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
#                               mixins.ListModelMixin, GenericViewSet):
#     queryset = LiveSubscription.objects.all()
#     serializer_class = LiveSubscriptionSerializer
#     permission_classes = [ApiKeyAuthentication]
#     lookup_field = 'chat_id'
