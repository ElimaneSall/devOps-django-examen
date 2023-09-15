from django import forms

from .models import  Hopital, Personne



class DocteurForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'password': forms.TextInput(attrs={'class': 'form-control input-md', }),
               }