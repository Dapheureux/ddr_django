
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('crm/', include('crm.urls')),
    path('actualite/', include('actualite.urls')),
    path('contact/', include('contact.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
