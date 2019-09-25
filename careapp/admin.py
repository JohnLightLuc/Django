# vim: set fileencoding=utf-8 :
from django.contrib import admin
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
from material.admin.decorators import register

from . import models



class HopitalAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'name',
        'email',
        'telephone',
        'adresse',
        'description',
        'image',
        'logo',
    )
    list_filter = (
        'date_add',
        'date_up',
        'id',
        'date_add',
        'date_up',
        'name',
        'email',
        'telephone',
        'adresse',
        'description',
        'image',
        'logo',
    )
    search_fields = ('name',)



class DocteurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'nom',
        'poste',
        'presentation',
        'facebook',
        'github',
        'twitter',
        'linkedin',
        'image',
        'hopital',
        'service',
    )
    list_filter = (
        'date_add',
        'date_up',
        'hopital',
        'service',
        'id',
        'date_add',
        'date_up',
        'nom',
        'poste',
        'presentation',
        'facebook',
        'github',
        'twitter',
        'linkedin',
        'image',
        'hopital',
        'service',
    )


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'titre',
        'description',
        'lien',
        'image',
    )
    list_filter = (
        'date_add',
        'date_up',
        'id',
        'date_add',
        'date_up',
        'titre',
        'description',
        'lien',
        'image',
    )


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'nom',
        'fonction',
        'image',
        'hopital',
    )
    list_filter = (
        'date_add',
        'date_up',
        'hopital',
        'id',
        'date_add',
        'date_up',
        'nom',
        'fonction',
        'image',
        'hopital',
    )



class TemoignageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'titre',
        'content',
        'client',
    )
    list_filter = (
        'date_add',
        'date_up',
        'client',
        'id',
        'date_add',
        'date_up',
        'titre',
        'content',
        'client',
    )



class CarteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'titre',
        'content',
        'image',
        'hopital',
    )
    list_filter = (
        'date_add',
        'date_up',
        'hopital',
        'id',
        'date_add',
        'date_up',
        'titre',
        'content',
        'image',
        'hopital',
    )



class Heure_travailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'jour',
        'heure_ouverture',
        'heure_fermeture',
        'hopital',
    )
    list_filter = (
        'date_add',
        'date_up',
        'hopital',
        'id',
        'date_add',
        'date_up',
        'jour',
        'heure_ouverture',
        'heure_fermeture',
        'hopital',
    )



class DeviseAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_up', 'message')
    list_filter = (
        'date_add',
        'date_up',
        'id',
        'date_add',
        'date_up',
        'message',
    )



class FormAppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_up',
        'nom',
        'email',
        'jour',
        'heure',
        'docteur',
        'message',
    )
    list_filter = (
        'date_add',
        'date_up',
        'docteur',
        'id',
        'date_add',
        'date_up',
        'nom',
        'email',
        'jour',
        'heure',
        'docteur',
        'message',
    )



class FormContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'telephone',
        'sujet',
        'message',
        'date_add',
    )
    list_filter = (
        'date_add',
        'id',
        'nom',
        'email',
        'telephone',
        'sujet',
        'message',
        'date_add',
    )



class FormSubscriptionAdmin(admin.ModelAdmin):

    list_display = ('id', 'email')
    list_filter = ('id', 'email')


def _register(model, admin_class):
    site.register(model, admin_class)


_register(models.Hopital, HopitalAdmin)
_register(models.Docteur, DocteurAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Client, ClientAdmin)
_register(models.Temoignage, TemoignageAdmin)
_register(models.Carte, CarteAdmin)
_register(models.Heure_travail, Heure_travailAdmin)
_register(models.Devise, DeviseAdmin)
_register(models.FormAppointment, FormAppointmentAdmin)
_register(models.FormContact, FormContactAdmin)
_register(models.FormSubscription, FormSubscriptionAdmin)
