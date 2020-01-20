from django.db import models


# Django ORM - Object Relational Mapper
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class Categoria(models.Model):
    title = models.CharField(max_length=255)
