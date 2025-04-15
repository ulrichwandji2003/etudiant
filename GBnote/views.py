from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



# @login_required
def couverture(request):
    
    
    return render(request, 'couverture/couverture.html')


def connexion(request):
    
    
    return render(request, 'couverture/connexion.html')


def dashboard(request):
    
    
    return render(request, 'couverture/dashboard.html')


def base(request):
    
    
    return render(request, 'base.html')