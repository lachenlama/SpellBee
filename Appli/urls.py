from django.urls import path
from . import views

urlpatterns =[
    path("", views.display, name='display'),
    path("reset/", views.reset, name='reset'),
]
