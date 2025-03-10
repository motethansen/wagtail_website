from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Command(BaseCommand):
    help = 'Automatically creates a superuser if it does not exist, using .env credentials'

    def handle(self, *args, **options):
        """
        Handles the automatic creation of a superuser if it does not exist.

        The method looks for the following environment variables:
        - DJANGO_SUPERUSER_USERNAME
        - DJANGO_SUPERUSER_EMAIL
        - DJANGO_SUPERUSER_PASSWORD

        If they are not defined, it defaults to 'admin' as the username,
        'admin@example.com' as the email and 'admin123' as the password.

        If the superuser already exists, it prints a warning message.

        If the superuser does not exist, it creates it and prints a success message.
        """

        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))