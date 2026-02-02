from django.db import models


class Tache(models.Model):
	"""Modèle représentant une tâche simple.

	Champs:
	- titre: texte (max 200 caractères)
	- terminee: booléen indiquant si la tâche est terminée (False par défaut)
	"""
	titre = models.CharField(max_length=200)
	terminee = models.BooleanField(default=False)

	def __str__(self):
		# Affichage lisible dans l'admin et les reprsentation texte
		etat = 'terminée' if self.terminee else 'en cours'
		return f"{self.titre} ({etat})"
