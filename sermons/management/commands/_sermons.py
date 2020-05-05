from django.contrib.staticfiles.storage import staticfiles_storage
from random import randint

from schedules.models import Event
from sermons.models import Sermon, sermon_types
from speakers.models import Speaker


def create_sermons():
    titles = [
        'Sermon No',
        'This is a not a very long title',
        'Title of a simple sermon',
        'This is another sermon that has a title',
        'Are we going to continue to invent more titles?',
        'Nop, this is it',
        'No more titles',
    ]

    for index in range(20):
        create_sermon(f'{titles[randint(0, len(titles)-1)]}: {index + 1}')


def create_sermon(title: str):
    events = Event.objects.all()
    url = staticfiles_storage.url('test-media/Daydream.mp3')
    speakers = Speaker.objects.all()
    speaker_amount = randint(1, 2)

    local_sermon = Sermon(
        event=events[randint(0, len(events)-1)],
        sermon_type=sermon_types[randint(0, len(sermon_types)-1)][0],
        title=title,
        audio_low=url,
        audio_med=url,
        audio_high=url,
        video_url='https://www.youtube.com/embed/aqz-KE-bpKQ',
        visible=bool(randint(0, 1))
    )
    local_sermon.save()
    for speaker in range(speaker_amount):
        local_sermon.speakers.add(speakers[randint(0, len(speakers)-1)])

    local_sermon.save()
