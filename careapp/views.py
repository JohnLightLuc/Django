from django.shortcuts import render
from .models import *
import datetime
from django import forms

# Create your views here.

class Visite(forms.Form):
    nom = forms.CharField(max_length=50)
    email = forms.EmailField()
    jour = forms.CharField(max_length= 50)
    periode = forms.TimeField()
    docteur = forms.ModelChoiceField(label= "docteur", queryset= Docteur.objects.all(), empty_label='---------')
    message = forms.Textarea()





#RECUPERATION DES DONNEES DE LA BASE DE DONNEE

#donnée hopital
hopital = Hopital.objects.get(pk=1)

#Message de liste defilant
devise = Devise.objects.all()
message = []
for dev in devise:
    message.append(dev.message)
#donnee de des cartes
card = Carte.objects.all()

#Heure de travail 
horaire = Heure_travail.objects.all()
date = datetime.datetime.now()
jour = date.strftime("%w")

empl = {
    'horaire': horaire,
    'jour': jour,
}

# Donnée service clinic 
service = Service.objects.all()

#DOCTORS

docteurs = Docteur.objects.all()

# TEMOIGNAGES

temoignages  = Temoignage.objects.all()

hopital = Hopital.objects.get(pk=1)
# LOAD DATA
data = {
    'hopital' : hopital,
    'devise': message,
    'carte': card,
    'empl': empl,
    'services': service,
    'docteurs': docteurs,
    'temoignages': temoignages,
}

#print(data.empl)


def index(request):
    message = 'Post encore eu de postes'
    if request.POST:
        
        
        try:
            new_visite = FormAppointment()
            new_visite.nom = request.POST.get('nom')
            new_visite.email = request.POST.get('email')
            new_visite.jour = request.POST.get('jour')
            new_visite.heure = request.POST.get('periode')
            new_visite.docteur = request.POST.get('docteur')
            new_visite.message = request.POST.get('message')
            new_visite.save()
            message= 'Demande nregistrée'        
        except:
            message= 'Veuillez bien remplir tous les champs'

        try:
            new_contact = FormContact()
            new_contact.nom = request.POST.get('nom')
            new_contact.email = request.POST.get('email')
            new_contact.telephone = request.POST.get('telephone')
            new_contact.sujet = request.POST.get('sujet')
            new_contact.message = request.POST.get('message')
            new_contact.save()
            message= 'Demande enregistrée'        
        except:
            message= 'Veuillez bien remplir tous les champs'

        try:
            new_mail = FormSubscription()
            new_mail.email = request.POST.get('email')
            new_mail.save()
            message= 'Veullez entrer uun email valide'         
        except:
            message= 'Veullez entrer uun email valide' 

    data['message'] = message

    return render(request, 'pages/index.html', data)


