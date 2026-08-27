from django.db import models

class Pizza(models.Model):

    name = models.CharField(max_length=200)
    toppings = models.ManyToManyField("Topping", blank=True)
    description = models.TextField(blank=True)
            
    def __str__(self):
        return self.name

class Topping(models.Model):

    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name    