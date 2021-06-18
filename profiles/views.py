from django.shortcuts import render
from .models import Profile

# Create your views here.
def profile_view(request,*args, **kwargs):
    # show all objects
    context = {
        "profiles" : Profile.objects.all()
    }
    return render(request,"profiles/profile_detail.html",context)