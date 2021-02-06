from django.utils import timezone
from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from churches.models import Church
from schedules.models import Event
from speakers.models import Speaker
from streams.models import Stream


class StreamsViewSet(mixins.ListModelMixin, GenericViewSet):
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

    queryset = Event.objects.filter(start__gt=timezone.now(), live_stream=True)
    serializer_class = EventSerializer

