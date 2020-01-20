from django.db import models


# Django ORM - Object Relational Mapper
class Post(models.Model):
    title = models.CharField(max_length=255)
    # null para o DB
    # blank para o form
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()


class Categoria(models.Model):
    title = models.CharField(max_length=255)
