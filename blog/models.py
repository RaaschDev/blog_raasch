from django.db import models
from datetime import datetime


class Post(models.Model):
    autor = models.CharField(max_length=155)
    titulo = models.CharField(max_length=155)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.titulo
