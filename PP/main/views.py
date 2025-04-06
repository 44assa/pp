from django.shortcuts import render

def main(request):
    return render(request, 'main/main-page.html')

def vacancy(request):
    return render(request, 'main/vacancy.html')

def firstVacancy(request):
    return render(request, 'main/firstVacancy.html')

def secondVacancy(request):
    return render(request, 'main/secondVacancy.html')

def application(request):
    return render(request, 'main/application.html')

def myApplication(request):
    return render(request, 'main/myApplication.html')

def entrance(request):
    return render(request, 'main/entrance.html')

def registration(request):
    return render(request, 'main/registration.html')

def profile(request):
    return render(request, 'main/profile.html')
