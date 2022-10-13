from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('realstate/',include('realstate.urls')),

] 


urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT  )# type: ignore