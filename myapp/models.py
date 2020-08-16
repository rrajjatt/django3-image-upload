from django.db import models
from django.conf.urls.static import static
from django.conf import settings

# Create your models here.
class ProductDetail(models.Model):
    product_name = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'myapp/images/' ,blank=True,null=True)