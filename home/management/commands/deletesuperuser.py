from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Command(BaseCommand):
    """
    Deletes the superuser specified by the environment variable 
    'DJANGO_SUPERUSER_USERNAME'. If the environment variable is not 
    set, defaults to 'admin'. If the superuser exists, deletes the 
    superuser and prints a success message. If the superuser does not 
    exist, prints a warning message.
    """
    help = 'Deletes the superuser specified in the .env file'

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')

        if User.objects.filter(username=username).exists():
            User.objects.get(username=username).delete()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" deleted successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" does not exist'))