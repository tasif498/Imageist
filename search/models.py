from django.db import models

# Create your models here.
class Products(models.Model):
    # _id=models.AutoField(primary_key=True)	
    colors=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    images=models.CharField(max_length=500)	
    price=models.CharField(max_length=500)
    product_link=models.CharField(max_length=500)
    sizes=models.CharField(max_length=500)
    sku=models.CharField(max_length=500)
    title=models.CharField(max_length=500)
    type=models.CharField(max_length=500)