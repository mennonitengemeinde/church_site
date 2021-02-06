from rest_framework import serializers

from churches.models import Church
from schedules.models import Event
from speakers.models import Speaker
from streams.models import Stream


# class ChurchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Church
#         fields = ['name', 'slug']


# class SpeakerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speaker
#         fields = ['name']


# class StreamSerializer(serializers.ModelSerializer):
#     speakers = SpeakerSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Stream
#         fields = ['id', 'title', 'speakers', 'live', 'live_mixlr_audio']



