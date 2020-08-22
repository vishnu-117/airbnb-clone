from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django_countries import countries
from django.core.paginator import Paginator
from .models import Room, RoomType, Amenity, Facility
from .forms import SearchForm


class HomeView(ListView):
    model = Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
    template_name = "rooms/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["now"] = timezone.now
        return context

    def get_absolute_url(self):
        # form django.core.urlresolvers import reverse
        # return reverse('', kwargs={'pk': self.pk})
        return '/potato'


class RoomDetail(DetailView):
    model = Room
    context_object_name = "room"
    template_name = 'rooms/room_detail.html'


class SearchView(View):
    def get(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            price = form.cleaned_data.get("price")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            beds = form.cleaned_data.get("beds")
            bedrooms = form.cleaned_data.get("bedrooms")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            aminities = form.cleaned_data.get("aminities")
            facility = form.cleaned_data.get("facility")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["beds__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            if instant_book is True:
                filter_args["instant_book"] = True

            if superhost is True:
                filter_args["host__superhost"] = True

            for amenity in amenities:
                filter_args["amenities"] = amenity

            for facility in facilities:
                filter_args["facilities"] = facility

            qs = Room.objects.filter(**filter_args)
            paginator = Paginator(qs, 10, orphans=5)
            page = request.GET.get("page", 1)
            rooms = paginator.get_page(page)
            return render(request, 'rooms/search.html', context={"rooms": rooms})
        else:
            form = SearchForm()
        return render(request, 'rooms/search.html', context={"form": form})
