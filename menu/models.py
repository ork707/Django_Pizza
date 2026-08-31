from django.db import models

class Pizza(models.Model):

    name = models.CharField(max_length=200)
    toppings = models.ManyToManyField("Topping", blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="pizzas/", blank=True)
    
            
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

class PizzaSize(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.pizza} - {self.size}" 