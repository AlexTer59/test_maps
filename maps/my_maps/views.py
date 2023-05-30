from django.shortcuts import render, redirect
import folium
import geocoder
from .models import Search
from .forms import SearcForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = SearcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearcForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat is None or lng is None:
        address.delete()
        return HttpResponse('Your address inputs is invalid')
    # Create map object
    m = folium.Map(location=[lat, lng], zoom_start=16)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # Get HTML Representation of Map obj
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)
