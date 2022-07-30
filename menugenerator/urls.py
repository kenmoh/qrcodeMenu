
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('menu.urls')),
    path('admin/', admin.site.urls),
]
