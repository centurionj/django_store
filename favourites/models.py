from django.db import models

from products.models import Product
from aut.models import User

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
