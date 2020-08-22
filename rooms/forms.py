from django import forms
from django_countries.fields import CountryField
from .models import Room, RoomType, Amenity, Facility


class SearchForm(forms.Form):
    city = forms.CharField()
    country = CountryField(default="IN").formfield()
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        required=False, queryset=RoomType.objects.all())
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    aminities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facility = forms.ModelMultipleChoiceField(
        queryset=Facility.objects.all(), widget=forms.CheckboxSelectMultiple)
