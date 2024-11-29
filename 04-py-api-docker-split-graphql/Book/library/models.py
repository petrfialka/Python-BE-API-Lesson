from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name
