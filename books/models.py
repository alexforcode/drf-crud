from django.db import models

from core.mixins.models import TimeStampMixin


class Author(TimeStampMixin, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ('last_name', )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(TimeStampMixin, models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('author', 'title')

    def __str__(self):
        return self.title