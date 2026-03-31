from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField()

    STATUS_CHOICES = [
        ('LIDO', 'Lido'),
        ('LENDO', 'Lendo'),
        ('QUERO_LER', 'Quero ler'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.titulo