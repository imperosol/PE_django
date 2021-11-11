from django.db import models


class Vaccin(models.Model):
    label = models.CharField(max_length=40)
    doses = models.PositiveIntegerField()

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save(update_fields=kwargs.keys())

    def __str__(self):
        return str(self.label)
