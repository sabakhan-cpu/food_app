from django.db import models

# Create your models/class here.
class Item(models.Model):
    
    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(max_length=100)
    item_price=models.FloatField()
    item_image=models.CharField(max_length=500,default="https://cdn-icons-png.flaticon.com/512/1147/1147805.png")

    #to get the items name instead object
    def __str__(self):
        return self.item_name
  
    