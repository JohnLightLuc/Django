from django.db import models

# Create your models here

# Class abstraite de date
class Modeldate(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class hopital
class Hopital(Modeldate):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length= 50)
    adresse = models.CharField(max_length=50)
    description = models.TextField(max_length= 500)
    image = models.ImageField(upload_to='images/hopital')
    logo = models.ImageField(upload_to='images/hopital')

    def __str__(self):
        return self.name

# class medecin
class Docteur(Modeldate):
    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    presentation = models.TextField(max_length=500)
    facebook = models.URLField()
    github = models.URLField()
    twitter= models.URLField()
    linkedin = models.URLField()
    image = models.ImageField(upload_to='images/docteur') 
    hopital = models.ForeignKey('Hopital', on_delete = models.CASCADE, related_name='hopital_medecin')
    service = models.ForeignKey('Service', on_delete = models.CASCADE, related_name='service_medecin')

    def __str__(self):
        return self.nom

# class de tous les services de l'hopital
class Service(Modeldate):
    titre = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    lien = models.URLField()
    image = models.ImageField(upload_to='images/services')

    def __str__(self):
        return self.titre
    
# Les client de l'hopital
class Client(Modeldate):
    nom = models.CharField(max_length=50)
    fonction = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    hopital = models.ForeignKey('Hopital', on_delete = models.CASCADE, related_name='hopital_doctor')

    def __str__(self):
        return self.nom

# Class  qui recueil les temoignages de client
class Temoignage(Modeldate):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    client = models.ForeignKey('Client', on_delete = models.CASCADE, related_name='client_temoin')

    def __str__(self):
        return self.titre

# Class  qui affiche donne les infos des cartes Emergency Case, Working Hours et Clinic Timetable
class Carte(Modeldate):
    titre = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/cartes')
    hopital = models.ForeignKey('Hopital', on_delete = models.CASCADE, related_name='hopital_med')

    def __str__(self):
        return self.titre

# class de reglage des heure de debut et de fin de travail
class Heure_travail(Modeldate):
    jour = models.CharField(max_length=20)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    hopital = models.ForeignKey('Hopital', on_delete = models.CASCADE, related_name='hopital_concerne')

# class qui contient le text defilant dans le home
class Devise(Modeldate):
    message = models.CharField(max_length=50)

# Formulaire de prise de rendez-vous
class FormAppointment(Modeldate):
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    jour = models.CharField(max_length=20)
    heure = models.CharField(max_length=50)
    docteur = models.CharField(max_length= 50)
    #docteur = models.ForeignKey('Docteur', on_delete= models.CASCADE, related_name='docteur_consult')
    message = models.TextField()

# Formulaire de contact
class FormContact(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

# Formulaire du mailing list
class FormSubscription(Modeldate):
    email = models.EmailField()








    
