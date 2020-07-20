from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "This Command Creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="himzei")
        if not admin:
            User.objects.create_superuser(
                "himzei", "himzei@naver.com", "judosa1820")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
