
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo/', include('core.urls')),
    path('auth/', include('auth2.urls')),
    path('admin/', admin.site.urls),
]

