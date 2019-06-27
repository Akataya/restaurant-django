from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    persons = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name
