from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def business_registration(request):
    return render(request, 'business_registration.html')

def business_login(request):
    return render(request, 'business_login.html')