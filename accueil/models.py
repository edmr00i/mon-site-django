from django.db import models


class Tache(models.Model):
	"""Modèle représentant une tâche simple.

	Ce modèle permet de créer et gérer des tâches avec un titre et un statut de
	complétion. Les tâches sont ordonnables et affichables facilement.

	Attributs:
		titre (CharField): Le titre ou description de la tâche (max 200 caractères).
		terminee (BooleanField): Booléen indiquant si la tâche est terminée.
							 Défaut: False.

	Méthodes:
		__str__(): Retourne une représentation lisible de la tâche avec son statut.
	"""
	titre = models.CharField(max_length=200)
	terminee = models.BooleanField(default=False)

	def __str__(self):
		# Affichage lisible dans l'admin et les reprsentation texte
		etat = 'terminée' if self.terminee else 'en cours'
		return f"{self.titre} ({etat})"
