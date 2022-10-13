
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    Realstate_create_view
)
urlpatterns = [
    path('',Realstate_create_view,name="realstate_create"),
    ] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)