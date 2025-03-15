from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='flowers/', blank=True, null=True)

    def __str__(self):
        return self.name
