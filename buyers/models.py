from django.db import models
from books.models import Book

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=30)


class BuyLog(models.Model):
    buyer_name = models.ForeignKey(
        to=Buyer,
        related_name="buyer",
        on_delete=models.CASCADE
    )
    bought_book = models.ForeignKey(
        to=Book,
        related_name="book",
        on_delete=models.CASCADE
    )

