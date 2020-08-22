from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Room


def all_rooms(request):
    page = request.GET.get("page")
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(page)
    except EmptyPage:
        rooms = paginator.page(1)

    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = Room.objects.all()[offset:limit]
    # page_count = ceil(Room.objects.all().count()/page_size)
    # return render(request, "rooms/home.html",
    #               context={"rooms": all_rooms,
    #                        "page": page,
    #                        "page_count": page_count,
    #                        "page_range": range(1, page_count),
    #                        })
    return render(request, "rooms/home.html",
                  context={"page": rooms})


def room_detail(request, pk):
    print(pk, "<<<<<")
    try:
        room = Room.objects.get(pk=pk)
        return render(request, 'rooms/room_detail.html', context={'room': room})
    except Room.DoesNotExist:
        raise Http404()

# def search(request):
#     citybool = request.GET.get("city")
#     country = request.GET.get("country")
#     room_type = request.GET.get("room_type")
#     city = str.capitalize(city)
#     price = int(request.GET.get("price", 0))
#     guests = int(request.GET.get("guests", 0))
#     bedrooms = int(request.GET.get("bedrooms", 0))
#     beds = int(request.GET.get("beds", 0))
#     baths = int(request.GET.get("baths", 0))
#     s_amenities = request.GET.getlist("amenities")
#     s_facilities = request.GET.getlist("facilities")
#     instant = bool(request.GET.get('instant'))
#     super_host = bool(request.GET.get('super_host'))

#     form = {
#         'city': city,
#         's_country': country,
#         's_room_type': room_type,
#         'price': price,
#         'guests': guests,
#         'bedrooms': bedrooms,
#         'beds': beds,
#         'baths': baths,
#         's_amenities': s_amenities,
#         's_facilities': s_facilities,
#         'instant': instant,
#         'super_host': super_host,
#     }
#     room_types = RoomType.objects.all()
#     amenities = Amenity.objects.all()
#     facilities = Facility.objects.all()
#     choices = {
#         'countries': countries,
#         'room_types': room_types,
#         'amenities': amenities,
#         'facilities': facilities,
#     }

#     filter_args = {}

#     if city != "Anywhere":
#         filter_args["city__startswith"] = city
#     if room_type != 0:
#         filter_args["room_type__pk"] = room_type
#     if price != 0:
#         filter_args['price__lte'] = price
#     if guests != 0:
#         filter_args['guests__gte'] = guests
#     if bedrooms != 0:
#         filter_args['bedrooms__gte'] = bedrooms
#     if beds != 0:
#         filter_args['beds__gte'] = beds
#     if baths != 0:
#         filter_args['baths__gte'] = baths
#     # if instant is True:
#     #     filter_args['instant_book'] = True
#     # if super_host is True:
#     #     filter_args['host'] = True
#     filter_args['country'] = country
#     rooms = Room.objects.filter(**filter_args)
