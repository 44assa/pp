from django.shortcuts import render

def main(request):
    return render(request, 'main/main-page.html')

def vacancy(request):
    return render(request, 'main/vacancy.html')
