from django.db import models
from orders.models import Order
from inventory.models import InventoryItem

   
    
class SoldItem(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete = models.PROTECT);
    order = models.ForeignKey(Order, on_delete = models.PROTECT);     