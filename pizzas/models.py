from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    #image_name_with_file_extension = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images/') #shouuld there be /pizzas before images/?

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=100)

    #Don't need this because Toppings is a regular plural, just a template:
    #class Meta:
    #    verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping_name
