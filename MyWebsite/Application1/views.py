from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photography(request):
    return render(request, 'photography.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request, 'contact.html')