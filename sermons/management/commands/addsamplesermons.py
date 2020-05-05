from django.core.management import BaseCommand

from ._sermons import create_sermons


class Command(BaseCommand):
    help = 'Adds sample sermons'

    def handle(self, *args, **options):
        create_sermons()
        self.stdout.write(self.style.SUCCESS('Successfully created sermons'))
