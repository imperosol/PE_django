from django.db import models
from django.contrib.auth.models import User, Group


class RegistrationRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    request_hour = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.first_name == "" and self.user.last_name == "":
            return self.user.username
        else:
            return f'{self.user.username} ({self.user.first_name} {self.user.last_name})'
