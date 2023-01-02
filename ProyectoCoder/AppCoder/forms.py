from django import forms

class CursoFormularios(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    numero_dia = forms.IntegerField()

class PersonaFormularios(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    DNI = forms.IntegerField()