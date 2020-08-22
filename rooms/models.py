from django.db import models
from django.urls import reverse
from core import models as core_models
from users import models as user_models
from django_countries.fields import CountryField
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstcract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Object Defination """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Object Defination """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Object Definatin """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Object Defination """

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """ Room Model Defination """

    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField(null=True)
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.CharField(max_length=30)
    guests = models.IntegerField(help_text="How many people will be stay")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    aminities = models.ManyToManyField(
        Amenity, related_name="rooms", blank=True)
    facility = models.ManyToManyField(
        Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        # Call the real save() method
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # from django.core.urlresolvers import reverse
        # return reverse('', kwargs={'pk': self.pk})
        return reverse('rooms:room_detail', kwargs={'pk': self.pk})

    def total_rating(self):
        all_review = self.reviews.all()
        all_rating = 0
        if len(all_review) > 0:
            for review in all_review:
                all_rating += review.rating_average()
            return all_rating / len(all_review)
        return 0

    def first_photo(self):
        photo, = self.photos.all()[:1]
        print(photo.file.url)
        return photo.file.url
        # print(self.photos.all())


class Photo(core_models.TimeStampedModel):

    """ Photo Model Defination """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="Rooms_Image")
    room = models.ForeignKey(
        Room, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
