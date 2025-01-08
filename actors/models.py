from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)

class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nacionality = models.CharField(
        max_length=100, 
        choices=NATIONALITY_CHOICES, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.name
    