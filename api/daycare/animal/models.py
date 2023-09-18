from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=32)
    species = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        if self.age == 1:
            return f"{self.name} the {self.species} is 1 year old"
        return f"{self.name} the {self.species} is {self.age} years old"

    
    def pet(self):
        return f"{self.name} is happy :)"