from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

# class Command(BaseCommand):
#     help = 'This is my first Custom Command.'
#
#     def handle(self, *args, **kwargs):
#         name = get_random_string(length=10)
#         self.stdout.write(name)

class Command(BaseCommand):
    help = "Random User Generator"

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help="The Number of Users to create.")
        parser.add_argument('-a', '--admin', action='store_true', help="Create Admin Accounts.")

    def handle(self, *args, **kwargs):
        qty = kwargs['qty']
        admin = kwargs['admin']

        for i in range(qty):
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if admin:
                User.objects.create_superuser(username=username, email='', password=password)
            else:
                User.objects.create_user(username=username, email='', password=password)


        if admin:
            self.stdout.write(f'{qty} Superuser accounts created successfully.')
        else:
            self.stdout.write(f'{qty} User accounts created successfully.')