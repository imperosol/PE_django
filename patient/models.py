from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.prenom} {self.nom}'
