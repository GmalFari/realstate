
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    register_view,
    profile
)

app_name="accounts"
urlpatterns = [
    path("signup",register_view,name="signup"),
    path("profile/<slug:slug>",profile,name="profile"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
