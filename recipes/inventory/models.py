from django.db import models
from products.models import Product


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return '{name} - {email}'.format(name=self.name, email=self.email) 
    
class Location(models.Model):
    """Location where inventories InventoryItem are stored. 
       Besides name and address, has a responsible manager and email.
       Later the manager and email fields may become a Foreign Keys from the Employees.
       """
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.name
    

class InventoryItem(models.Model):
    
    product = models.ForeignKey(Product, related_name = 'inventory_items', on_delete = models.PROTECT);
    amount = models.PositiveSmallIntegerField(default = 1);
    registered_at = models.DateField(auto_now_add=True);
    # DateField
    cost = models.DecimalField(max_digits=7, decimal_places=2, default = '0');
    sell_by = models.DateField(null=True, blank=True);
    location = models.ForeignKey(Location, related_name = 'inventory_items', on_delete = models.PROTECT);
    manufacturer = models.ForeignKey(Manufacturer, related_name = 'inventory_items', on_delete = models.PROTECT);
    
         
    '''
    Displays info in admin page
    '''
    def __str__(self) -> str:
        return '{product} - {sell_by} - Amount: {amount} - Cost: {cost} - {location}'.format(product=self.product, sell_by=self.sell_by, 
                                                                                amount=self.amount, cost=self.cost,
                                                                                  location=self.location)

class LossInventory(models.Model):
    product = models.ForeignKey(Product, related_name = 'inventory_loss', on_delete = models.CASCADE);
    amount = models.PositiveSmallIntegerField(default = 1);
    cost = models.DecimalField(max_digits=7, decimal_places=2, default = '0');
    location = models.ForeignKey(Location, related_name = 'inventory_loss', on_delete = models.CASCADE);
    manufacturer = models.ForeignKey(Manufacturer, related_name = 'inventory_loss', on_delete = models.CASCADE);