from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(to=Genre, null=True, blank=True, verbose_name='Жанр', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.genre.title}"