from django.db import models
from django.db.models.deletion import DO_NOTHING


class Book(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name


class Borrow(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=DO_NOTHING)
    user = models.UUIDField()

    def __str__(self) -> str:
        return f"Borrow of book {self.book} from {self.start} to {self.end}"
