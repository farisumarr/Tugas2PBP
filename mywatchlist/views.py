from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


def show_watchlist(request):
    data_watchlist = MyWatchList.objects.all()

    watched = 0
    unwatched = 0

    for i in data_watchlist:
        if i.watched=="yes":
            watched+=1
        elif i.watched=="no":
            unwatched+=1

    context = {
        'nama': 'Muhammad Faris Umar Rahman',
        'npm': '2106702402',
        'list_watchlist': data_watchlist
    }
    
    if (watched > unwatched):
        return render(request, "mywatchlist_banyak.html", context)
    else:
        return render(request, "mywatchlist_sedikit.html", context)
    # return render(request, "mywatchlist.html", context)

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

