from django.db import models


class Centre(models.Model):
    label = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return str(self.label)
