from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class Promocode(models.Model):
    code = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class PromocodeProduct(models.Model):
    promocode = models.ForeignKey(Promocode, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('promocode', 'product')
