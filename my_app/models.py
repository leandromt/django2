from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.title


# Django ORM - Object Relational Mapper
class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name='Título')

    # null para o DB
    # blank para o form
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='conteúdo')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    categorias = models.ManyToManyField(Categoria, verbose_name='Categorias')

    class Meta:
        verbose_name = 'Artigo'
        #verboso_name_plural = 'Artigos'

    def __str__(self):
        return self.title
