from django.db import models

class utilizadores(models.Model):
    id = models.PositiveIntegerField().primary_key
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome


# Create your models here.
