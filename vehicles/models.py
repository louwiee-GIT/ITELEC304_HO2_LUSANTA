from django.db import models


# Parent Model
class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {self.price}"

    def __str__(self):
        return self.brand


# Child Model 1
class Car(Vehicle):
    doors = models.IntegerField()

    # Method overriding
    def vehicle_info(self):
        return f"{self.brand}  with {self.doors} doors costs {self.price}"


# Child Model 2
class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=False)

    # Method overriding
    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self.price}"