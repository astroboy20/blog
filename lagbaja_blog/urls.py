
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('superback/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]
