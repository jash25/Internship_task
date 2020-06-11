from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return self.name
# Create your models here.
