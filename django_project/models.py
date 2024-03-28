from django.db import models

class Product(models.Model):
    sku_id = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name