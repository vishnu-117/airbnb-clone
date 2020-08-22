from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    # def add_arguments(self, parser):
    #     """
    #     Entry point for subclassed commands to add custom arguments.
    #     """
    #     parser.add_argument(
    #         "--times", help="How many times do you loves me?"
    #     )

    # def handle(self, *args, **options):
    #     times = options.get("times")
    #     for i in range(0, int(times)):
    #         print("i love you")
    def handle(self, *args, **options):
        amenity = [
            "Kitchen",

            "Shampoo",

            "Heating",

            "Air conditioning",

            "Washing machine",

            "Dryer",

            "Wifi",

            "Breakfast",

            "Indoor fireplace"

            "Hangers"

            "Iron",

            "Hair dryer",

            "Laptop-friendly workspace",

            "TV",
            "Cot",

            "High chair",

            "Self check-in",

            "Smoke alarm", ]

        for a in amenity:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("amenity is created"))
