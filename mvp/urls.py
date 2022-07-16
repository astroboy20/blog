from django.urls import path
from . import views

urlpatterns = [
    path('email', views.send_prelaunch_email),
]
