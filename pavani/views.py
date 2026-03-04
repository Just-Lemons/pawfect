from django.shortcuts import render
from pavani.models import Pets

def details(request,pet_id):
    #Fetching data from database
    Pet = Pets.objects.get(pk=pet_id)
    context = {
        'Pets' : Pet
    }
    return render(request,'details.html',context)


    