from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from churches.models import Church
from schedules.models import Event
from speakers.models import Speaker
from streams.models import Stream


class StreamsList(APIView):
    def get(self, request):
        class EventSerializer(serializers.ModelSerializer):
            class ChurchSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Church
                    fields = ['name', 'slug']

            class StreamSerializer(serializers.ModelSerializer):
                class SpeakerSerializer(serializers.ModelSerializer):
                    class Meta:
                        model = Speaker
                        fields = ['name']

                speakers = SpeakerSerializer(many=True, read_only=True)

                class Meta:
                    model = Stream
                    fields = ['id', 'title', 'speakers', 'live', 'live_mixlr_audio']

            streams = StreamSerializer(many=True, read_only=True)
            church = ChurchSerializer(read_only=True)

            class Meta:
                model = Event
                fields = ['id', 'title', 'start', 'end', 'church', 'streams']

        queryset = Event.objects.filter((Q(start__gt=timezone.now()) & Q(live_stream=True)) | Q(streams__live=True))
        serializer_class = EventSerializer(queryset, many=True)
        return Response(serializer_class.data)


