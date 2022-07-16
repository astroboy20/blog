
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('superback/', admin.site.urls),
    path('', views.home),
    path('auth/', include('authentication.urls')),
]
