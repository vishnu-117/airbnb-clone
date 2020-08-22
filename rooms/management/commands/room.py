import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models
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
        all_users = user_models.User.objects.all()
        room_type = room_models.RoomType.objects.all()
        seeder.add_entity(room_models.Room, number, {
            'address': lambda x: seeder.faker.address(),
            'guests': lambda x: random.randint(0, 7),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_type),
            'price': lambda x: random.randint(0, 3000),
            'guests': lambda x: random.randint(0, 7),
            'beds': lambda x: random.randint(0, 7),
            'bedrooms': lambda x: random.randint(0, 7),
            'baths': lambda x: random.randint(0, 7),
        })
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        aminities = room_models.Amenity.objects.all()
        facility = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp"
                )

            for a in aminities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.aminities.add(a)
            for f in facility:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(f)
            for r in house_rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS("room is created"))
