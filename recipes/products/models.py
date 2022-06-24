from django.db import models


class Group(models.Model):
    """ The name field has to be unique, so to avoid duplicates. 
        Has zero or many Products.
        Created by admin only.
        """   
    name = models.CharField(max_length=40, unique=True)
    pic = models.ImageField(upload_to='images/', null=True, default = 'null');
    
    def get_products_count(self):
        return Product.objects.filter(group=self).count()
    
    def __str__(self) -> str:
        return '{name}'.format(name=self.name) 


class Product(models.Model):
    """ May be associated with only one Category, which is not null.
        Created by admin only.
        The related_name parameter will be used to create a reverse relationship 
        where the Category instances will have access a list of Product instances 
        that belong to it.
        """
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, related_name='products', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    weight = models.DecimalField(max_digits=7, decimal_places=2);
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0);
    pic = models.ImageField(upload_to='images/', null=True, default = 'null');
    
    def is_available(self):
        from inventory.models import InventoryItem
        available_amount = InventoryItem.objects.filter(product=self).count()
        return available_amount
    
    def __str__(self) -> str:
        return '{name} - {group}'.format(name=self.name, group=self.group) 
    
    
    def is_instock(self):
        """ returns not negtive number, how much units of the product is in stock (inventory)
            """
        from inventory.models import InventoryItem
        inventory = InventoryItem.objects.filter(product=self)
        instock = 0
        for inv in inventory:
            instock+=inv.amount
        return instock
            

    
