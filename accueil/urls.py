from django.urls import path
from .views import liste_taches, ajouter_tache

app_name = 'accueil'

urlpatterns = [
    path('', liste_taches, name='liste_taches'),
    path('ajouter/', ajouter_tache, name='ajouter_tache'),
]