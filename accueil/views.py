from django.shortcuts import render
from datetime import date, datetime
from .forms import NomForm
from .models import Tache

def index(request):
    """Vue index qui affiche un message dépendant de l'heure et gère un formulaire de nom."""
    # Déterminer le salut selon l'heure locale (module datetime demandé)
    maintenant = datetime.now()
    if maintenant.hour < 12:
        greeting = "Bon matin"
    else:
        greeting = "Bon après-midi"

    # Valeur par défaut du message
    message = f"{greeting} !"
    nom = None

    if request.method == "POST":
        form = NomForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            # Message personnalisé avec le nom
            message = f"{greeting}, {nom} !"
    else:
        form = NomForm()

    # Récupérer les tâches depuis la base, ordonnées par titre
    tasks = Tache.objects.order_by('titre')

    contexte = {
        'message': message,
        'date_du_jour': date.today(),
        'form': form,
        'tasks': tasks,
    }
    return render(request, 'accueil/index.html', contexte)