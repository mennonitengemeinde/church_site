from django.core.management import BaseCommand

from schedules.management.commands._events import create_events


class Command(BaseCommand):
    help = 'Adds sample events'

    def handle(self, *args, **options):
        create_events()
        self.stdout.write(self.style.SUCCESS('Successfully created events'))
