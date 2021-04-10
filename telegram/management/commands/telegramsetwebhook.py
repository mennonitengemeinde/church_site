import time

from django.conf import settings
from django.core.management import BaseCommand

import telebot


class Command(BaseCommand):
    help = 'Sets Telegram Webhook'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.WOL_EVENTS_BOT_TOKEN)
        bot.remove_webhook()
        time.sleep(0.1)
        # bot.set_webhook(
        #     url=settings.WOL_EVENTS_BOT_BASE_URL + 'telegram/webhook/' + settings.WOL_EVENTS_BOT_TOKEN + '/',
        #     certificate=open(WEBHOOK_SSL_CERT, 'r')
        # )
        bot.set_webhook(
            url=settings.WOL_EVENTS_BOT_BASE_URL + 'telegram/webhook/' + settings.WOL_EVENTS_BOT_TOKEN + '/'
        )
        self.stdout.write(self.style.SUCCESS('Successfully set webhook'))
