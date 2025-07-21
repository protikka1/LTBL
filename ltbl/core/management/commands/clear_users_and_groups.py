from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "Delete all groups and non-superuser users"

    def handle(self, *args, **kwargs):
        Group.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write(
            self.style.SUCCESS(
                "All groups and non-superuser users deleted."
            )
        )
