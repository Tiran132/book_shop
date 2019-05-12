from django.db import models
from categories.models import Category


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    img = models.CharField(max_length=10000)
    category = models.ForeignKey(
        to=Category,
        related_name="books",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
