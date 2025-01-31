from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import*
from .models import*
import json


# Create your views here.


def envoi(request):
    if request.method=='POST':
        
        if 'FormDonnee' in request.POST:
            form_donnee = FormDonnee(request.POST)
            if form_donnee.is_valid():
            
                nom = request.POST.get('nom')
                prenom = request.POST.get('prenom')
                email = request.POST.get('email')
                sexe = request.POST.get('sexe')
                age=request.POST.get('age')
            
                initial_data = {
                    'nom':nom,
                    'prenom':prenom,
                    'email':email,
                    'sexe':sexe,
                    'age':age
                            }

#--------------Remplissage automatique du deuxieme formulaire
                form_rdv = FormRdv(initial=initial_data)
            return render(request, 'Rendezvous.html',{'form':form_rdv})
            
        elif 'FormRdv' in request.POST:
            form_donnee = FormDonnee(request.POST)
            if form_donnee.is_valid():
                form_donnee.save()
            return HttpResponseRedirect('confirmation')
            
    else:
        form_donnee = FormDonnee()
        return render(request,'patient.html',{})
    


            

    
    
def confirmation(request):
    return render(request,'confirmation.html')
