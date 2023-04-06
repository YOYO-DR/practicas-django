from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('votar/',votacion,name='votar'),
    path('votaciones/',votaciones,name='votaciones'),
]
