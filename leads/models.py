from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tipo'

    def __str__(self):
        return self.nome


class Lead(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.CharField(max_length=255, verbose_name='Email')
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, verbose_name='Tipo')
    vidas = models.IntegerField(verbose_name='Quantidade de vida')

    class Meta:
        verbose_name = 'Lead'

    def __str__(self):
        return self.nome