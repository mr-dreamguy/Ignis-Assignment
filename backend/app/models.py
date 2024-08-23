from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    mrp = models.CharField(max_length=50)
    weekly_sale = models.CharField(max_length=50)
    description = models.TextField()
    fit = models.CharField(max_length=100, null=True)
    fabric = models.CharField(max_length=100, null=True)
    pattern = models.CharField(max_length=100, null=True)
    neck = models.CharField(max_length=100, null=True)
    sleeve = models.CharField(max_length=100, null=True)
    length = models.CharField(max_length=100, null=True)
    waistrise = models.CharField(max_length=100, null=True)
    waistband = models.CharField(max_length=100, null=True)
    bottomwearlength = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Variant(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=50)
    image = models.URLField(max_length=200, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    
    def __str__(self):
        return self.color
    
class VariantData(models.Model):
    id = models.BigAutoField(primary_key=True)
    size = models.CharField(max_length=10)
    quantity = models.CharField(max_length=50)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name="data")

    def __str__(self):
        return self.size