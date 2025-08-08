from django.db import models
from django.utils import timezone

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    membro = models.ForeignKey('membros.Membro', on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.membro} inscrito em {self.evento}'