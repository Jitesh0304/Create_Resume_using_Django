from django.urls import path
from . import views


urlpatterns = [
    path('serv/', views.servicepage, name='service'),
]
