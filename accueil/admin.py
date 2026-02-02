from django.contrib import admin
from .models import Tache


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
	list_display = ('titre', 'terminee')
	list_filter = ('terminee',)
	search_fields = ('titre',)
