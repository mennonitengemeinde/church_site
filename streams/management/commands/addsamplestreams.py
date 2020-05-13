from django.core.management import BaseCommand

from ._streams import create_streams


class Command(BaseCommand):
    help = 'Adds some sample streams'

    def handle(self, *args, **options):
        create_streams()
        self.stdout.write(self.style.SUCCESS('Successfully created streams'))
