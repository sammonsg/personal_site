from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('about/', include('about.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
