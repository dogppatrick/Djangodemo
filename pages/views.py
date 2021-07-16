from django.shortcuts import render
from django.http import HttpResponse
import folium

districts = {
        0:{
          0: [25.155491, 121.632979]
         ,1: [25.152155, 121.632515]
         ,2: [25.160204, 121.640730]
        },
        1:{
          0: [25.005491, 121.042979]
         ,1: [25.003155, 121.038515]
         ,2: [25.000204, 121.040730]
        },
        2:{
          0: [24.955491, 121.532979]
         ,1: [24.961155, 121.532515]
         ,2: [24.960204, 121.535730]
        },
    }
districts_name= [f"第{d}天" for d in "一二三"]

def get_fmap(user_agent, center_point,marker_points):
    if 'Mobile' in user_agent:
        fmap = folium.Map(width=150, height=100, location=center_point, zoom_start=15)
    else:
        fmap = folium.Map(width=600, height=350, location=center_point, zoom_start=15)
    for point in marker_points:
        folium.Marker(marker_points[point], icon=folium.Icon(color='red'),popup=f'point {point},{marker_points[point]}').add_to(fmap)
    fmap = fmap._repr_html_()
    return fmap

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    context = {
        "title": "title",
    }
    return render(request,"home.html",context)

def fmap_view(request,distict=0,*args, **kwargs):
    
    dist_tmp = districts.get(distict,0)
    center_point = [sum([point[0] for point in dist_tmp.values()])/len(dist_tmp),sum([point[1] for point in dist_tmp.values()])/len(dist_tmp)]
    user_agent = request.headers['user-agent']

    fmap = get_fmap(user_agent, center_point,dist_tmp)
    context = {
        "title": "fmap_test",
        "map": fmap ,
        "distinct":  [[districts_name[d],d] for d in districts.keys()]
    }

    return render(request,"fmap.html",context)

def fmap_detail_view(request,distict=0,point=0,*args, **kwargs):
    dist_tmp = districts.get(distict,0)
    lat_tmp = dist_tmp.get(point,0)
    user_agent = request.headers['user-agent']
    fmap = get_fmap(user_agent, lat_tmp,dist_tmp)
    context = {
        "title": "fmap_test",
        "map": fmap,
        "cur_distict":distict,
        "distinct": [[districts_name[d],d] for d in districts.keys()],
        "points":[[d,d] for d in dist_tmp.keys()]
    }
    return render(request,"fmap_detail.html",context)