from django.db import models


class Borrow(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    book = models.IntegerField()
    user = models.UUIDField()

    def __str__(self) -> str:
        return f"Borrow of book {self.book} from {self.start} to {self.end}"
