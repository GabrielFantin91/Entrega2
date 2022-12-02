from django.db import models

# Create your models here.
class Area(models.Model):
    nombre=models.CharField(max_length=50)
    numero=models.IntegerField()
    def __str__(self):
        return self.nombre+" "+str(self.numero)
    

class trabajador (models.Model):
    nombre=models.CharField(max_length=30, default='SOME STRING')
    apellido=models.CharField(max_length=30, default='SOME STRING')
    def __str__(self):
        return self.nombre+" "+self.apellido

class encargado (models.Model):
    nombre=models.CharField(max_length=30, default='SOME STRING')
    apellido=models.CharField(max_length=30, default='SOME STRING')
    email=models.EmailField(max_length=30, default='SOME STRING')
    profesion=models.CharField(max_length=30, default='SOME STRING')
    def __str__(self):
        return self.nombre+" "+self.apellido


        