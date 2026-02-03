from django.test import TestCase
from .models import Tache


class TacheModelTest(TestCase):
    """Tests unitaires pour le modèle Tache."""

    def test_tache_str_method(self):
        """Vérifie que la méthode __str__ retourne le titre avec l'état."""
        # Créer une tâche non terminée
        tache = Tache.objects.create(titre="Faire les courses", terminee=False)
        self.assertEqual(str(tache), "Faire les courses (en cours)")

        # Créer une tâche terminée
        tache_terminee = Tache.objects.create(titre="Étudier Django", terminee=True)
        self.assertEqual(str(tache_terminee), "Étudier Django (terminée)")
