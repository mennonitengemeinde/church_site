from random import randint

from schedules.models import Event
from speakers.models import Speaker
from streams.models import Stream

desc = 'This is a Stream description that is to demo the description placement'

titles = (
    'This is a Stream title',
    'This is another stream title',
    'Ok, another title',
    'Yep, one more title for live streams',
    'Lets try another stream title to mix it up',
    'Last title I guess',
)


def create_streams():
    for i in range(20):
        create_stream(f'{titles[randint(0, len(titles)-1)]}:{i+1}')


def create_stream(title: str):
    events = Event.objects.all()
    speakers = Speaker.objects.all()
    speaker_amount = randint(1, 2)
    local_stream = Stream(
        event=events[randint(0, len(events)-1)],
        title=title,
        description=desc,
        live_url='https://www.youtube.com/embed/aqz-KE-bpKQ',
        live_mixlr_audio=bool(randint(0, 1)),
        live=bool(randint(0, 1))
    )
    local_stream.save()

    for i in range(speaker_amount):
        local_stream.speakers.add(speakers[randint(0, len(speakers)-1)])

    local_stream.save()
