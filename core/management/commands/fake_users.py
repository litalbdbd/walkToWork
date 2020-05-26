import silly
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        for x in range(100):
            o, c = User.objects.get_or_create(
                username=silly.firstname()
            )
