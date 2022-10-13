from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse

from .models import Profile

# from .forms import MyUserCreationForm



# Create your views here.
def register_view(request):
    pass
#     form = MyUserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.save()
#         return HttpResponse("")
#     return render(request,"registration/signup.html",{
#         "form":form
#     })
 

def profile(request,slug):
    try:
        profile = Profile.objects.get(slug=slug)
    except:
        profile = None
    if profile is None:
        HttpResponse("Not found")
    print(profile) 
    context= {"profile":profile}
    return render(request,"registration/profile.html",context=context)