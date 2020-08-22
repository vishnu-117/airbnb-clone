from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings


class User(AbstractUser):
    """ Custom User Model"""

    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    LANGUAGE_CHOICE = (
        ("English", "Englisth"),
        ("Hindi", "Hindi"),
        ("Gujarati", "Gujarati"),
    )
    CURRENCY_CHOICE = (
        ("USD", "USD"),
        ("Ruppy", "Ruppy"),
    )
    avatar = models.ImageField(upload_to="Avatar", null=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, null=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=15, null=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=10, null=True, blank=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        if email_verified is False:
            secret = uuid.uuid4.hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Airbnb account",
                f"Verify account, this is your secret :{secret}",
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )
        return
