from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    item_price=models.FloatField(default=0.0)
    size=models.CharField(default=0,max_length=10)


    def __str__(self):
        return self.item.item_name
