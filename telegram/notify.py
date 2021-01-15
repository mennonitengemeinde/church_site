from django.conf import settings
import requests

from telegram.models import LiveSubscription


def send_going_live_notification():
    subs = LiveSubscription.objects.all()
    context = {subs: []}
    for sub in subs:
        context['subs'].append(sub.chat_id)
    requests.post(settings.BOT_URL + '/notify/live', data=context)
