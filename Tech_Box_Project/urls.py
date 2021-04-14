from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('app_auth.urls')),
    path('gadgets/', include('app_gadgets.urls')),
]
