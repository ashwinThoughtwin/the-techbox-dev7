from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "This Command Will Create Superuser."

    def handle(self, *args, **kwargs):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        User.objects.create_superuser(username=username, email='', password=password)
        self.stdout.write('Superuser account created successfully.')