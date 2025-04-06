from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('firstVacancy', views.firstVacancy, name='firstVacancy'),
    path('secondVacancy', views.secondVacancy, name='secondVacancy'),
    path('application', views.application, name='application'),
    path('myApplication', views.myApplication, name='myApplication'),
    path('entrance', views.entrance, name='entrance'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile')
]
