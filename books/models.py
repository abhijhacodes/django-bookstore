from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=256)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f'{self.id}> {self.title}'


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
