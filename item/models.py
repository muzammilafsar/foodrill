from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=30)
    item_description=models.TextField(max_length=100,default='this is the description')
    item_price=models.FloatField(default=0.0)
    item_price_sml=models.FloatField(default=0.0)
    item_price_md=models.FloatField(default=0.0)
    item_price_lrg=models.FloatField(default=0.0)
    item_url=models.URLField(default='#')



    def __str__(self):
        return self.item_name

