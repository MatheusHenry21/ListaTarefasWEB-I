from django.db import models

class Taferas(models.Model):
    nome = models.CharField(max_length=50)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome