from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api_view.urls")),
]
from django.urls import path

