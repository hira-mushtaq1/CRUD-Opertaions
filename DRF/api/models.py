from django.db import models

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length=255, default="technology")
    subcategory = models.CharField(max_length=255, default="AC")
    name = models.CharField(max_length=255, default="orient")
    amount = models.PositiveIntegerField()
 
    def __str__(self) -> str:
        return self.name