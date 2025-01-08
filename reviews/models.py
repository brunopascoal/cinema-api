from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

class Reviews(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    rate = models.IntegerField(
        validators=[
            MinValueValidator(0, "Value can't be less than zero"),
            MaxValueValidator(5, "Value can't be greater than five")
        ]
    )
    comment = models.TextField(null=True, blank=True)