from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        """
        parser.add_argument(
            "--number", default=1, type=int, help="How many times do you loves me?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            "is_staff": False,
            "is_superuser": False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("user is created"))
