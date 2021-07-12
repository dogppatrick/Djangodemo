from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    context = {
        "title": "title",
    }
    return render(request,"home.html",context)


def fmap_view(request,point=0,*args, **kwargs):
    lat_dict = {
         0: [25.055491, 121.532979]
        ,1: [25.052155, 121.532515]
        ,2: [25.060204, 121.540730]
    }
    lat_tmp = lat_dict.get(point,0)
    fmap = folium.Map(width=800, height=500, location=lat_tmp, zoom_start=15)
    for point in lat_dict:
        folium.Marker(lat_dict[point], icon=folium.Icon(color='red'),popup='lol').add_to(fmap)
    fmap = fmap._repr_html_()
    context = {
        "title": "fmap_test",
        "map": fmap
    }
    print(request)
    return render(request,"fmap.html",context)