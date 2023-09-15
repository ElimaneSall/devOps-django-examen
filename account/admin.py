from django.contrib import admin

# Register your models here.
from .models import  Personne, Visit

admin.site.register(Personne)
admin.site.register(Visit)
