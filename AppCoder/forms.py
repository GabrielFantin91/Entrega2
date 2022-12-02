from django import forms
 

class areaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    numero=forms.IntegerField()


class encargadoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)

