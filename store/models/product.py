from django.db import models
from .category import Categories

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    desciption = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to="upload/products/")

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()
        
    def __str__(self):
        return f"{self.name}"