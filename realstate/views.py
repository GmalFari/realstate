from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

from .forms import ImageRealstateForm, RealstateForm
from .models import Realstate, RealstateImage


# Create your views here.
def Realstate_create_view(request):
    
    form = RealstateForm(request.POST or None)
    files = request.FILES.getlist('image')
    if form.is_valid()  :
        com_obj = form.save(commit=False)
        com_obj.company = request.user
        com_obj.save()
        for file in files:
            RealstateImage.objects.create(company=com_obj,image=file)
        messages.success(request,"New realstate added")    
        return HttpResponseRedirect('/')
    else:
        print(form.errors)
    images= RealstateImage.objects.all()
    context={
        "form":RealstateForm(),
        "imgsform":ImageRealstateForm(),
        'images': images
    }
    
    return render(request,"realstate/index.html",context=context)
