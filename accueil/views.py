from django.shortcuts import redirect, render
from datetime import date, datetime
from .forms import TacheForm
from .models import Tache


def _get_greeting_message():
    """Génère un message de salutation selon l'heure locale.

    Returns:
        str: \"Bon matin\" avant midi, \"Bon après-midi\" sinon.
    """
    maintenant = datetime.now()
    if maintenant.hour < 12:
        return "Bon matin"
    else:
        return "Bon après-midi"


def liste_taches(request):
    """Affiche la liste des tâches et le formulaire d'ajout.

    Cette vue traite uniquement les requêtes GET pour afficher la liste des tâches
    et le formulaire vierge pour en ajouter une nouvelle. Elle affiche également
    un message de salutation basé sur l'heure locale.

    Args:
        request (HttpRequest): L'objet requête HTTP de type GET.

    Returns:
        HttpResponse: Réponse HTTP contenant la page index.html avec le contexte.

    Contexte du template:
        message (str): Message de salutation (\"Bon matin\" ou \"Bon après-midi\").
        date_du_jour (date): La date actuelle.
        form (TacheForm): Le formulaire vierge pour créer une nouvelle tâche.
        tasks (QuerySet): Liste des tâches ordonnées par titre.
    """
    message = f"{_get_greeting_message()} !"
    form = TacheForm()
    tasks = Tache.objects.order_by('titre')

    contexte = {
        'message': message,
        'date_du_jour': date.today(),
        'form': form,
        'tasks': tasks,
    }
    return render(request, 'accueil/index.html', contexte)


def ajouter_tache(request):
    """Traite l'ajout d'une nouvelle tâche via le formulaire.

    Cette vue traite uniquement les requêtes POST pour valider et sauvegarder
    une nouvelle tâche. Après l'ajout réussi, elle redirige vers la liste des tâches.

    Args:
        request (HttpRequest): L'objet requête HTTP contenant les données POST
                               du formulaire TacheForm.

    Returns:
        HttpResponseRedirect: Redirection vers la vue liste_taches après ajout réussi.
        HttpResponse: Si le formulaire n'est pas valide, affiche la page avec
                     les erreurs de formulaire.
    """
    if request.method == "POST":
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil:liste_taches')
        else:
            # Si le formulaire est invalide, afficher la liste avec les erreurs
            message = f"{_get_greeting_message()} !"
            tasks = Tache.objects.order_by('titre')
            contexte = {
                'message': message,
                'date_du_jour': date.today(),
                'form': form,
                'tasks': tasks,
            }
            return render(request, 'accueil/index.html', contexte)
    else:
        # Si ce n'est pas un POST, rediriger vers la liste
        return redirect('accueil:liste_taches')