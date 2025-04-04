from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('vacancy', views.vacancy)
]
