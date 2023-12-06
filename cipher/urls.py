from django.urls import path

from . import views

urlpatterns = [
    path("", views.cipher),
    # path('encrypt/', views.encrypt_view),
    # path('decrypt/', views.decrypt_view),
    path('index.html', views.cipher, name='index'),
    path('dhe.html', views.dhe, name='dhe'),

]