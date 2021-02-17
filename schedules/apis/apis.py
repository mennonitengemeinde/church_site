# from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from schedules.models import Event
#
#
# class EventsListApi(APIView):
#     class OutputSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Event
#             fields = ('church', 'start', 'end', 'title', 'description', 'address', 'map_search_query', 'in_person')
