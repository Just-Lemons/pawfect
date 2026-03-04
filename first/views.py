from django.http import HttpResponse
from django.shortcuts import render
from pavani.models import Pets

def home(request):
    #Fetching data from database
    data = Pets.objects.all()
    context = {
        'Pets' : data
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    