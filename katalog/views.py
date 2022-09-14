from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'nama': 'Muhamamd Faris Umar Rahman',
    'npm' : '2106702402',
    'list_barang': data_barang_katalog
}
    return render(request, "katalog.html", context)
