from email.mime import image
from django.contrib import messages
from django.shortcuts import render,HttpResponse
from .models import Realstate,RealstateImage
from .forms import RealstateForm,ImageRealstateForm
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
        return HttpResponse("created")
    else:
        print(form.errors)
    context={
        "form":RealstateForm(),
        "imgsform":ImageRealstateForm(),
    }
    images= RealstateImage.objects.all()
    context['images']= images
    return render(request,"realstate/index.html",context=context)
        # for img in files:
        #     RealstateImage.objects.create(realstate_image=img,company=com_obj)
   

    
        # imgs = request.FILES.getlist('imgs')
        # for img in imgs:
        #     RealstateImage.objects.create(realstate_image=img)

        # com_obj = form.save(commit=False)
        # com_obj.company = request.user
        # com_obj.save()
        # imgs_obj = imgsform.save(commit=False)
        # imgs_obj.realstate = instance
        # imgs_obj.save()