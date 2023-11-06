from django.urls import path

from . import views

urlpatterns = [
    path("", views.cipher, name="cipher"),
    path('index.html', views.cipher, name='index'),
]