from django.db import models
#from products.models import PricedProduct
from products.models import Product
    
class Order(models.Model):
    """Customer is a user who placed this order;
    User may not be deleted if he has orders;
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    inventory_total_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0);
    
    def get_total(self):
        return sum(ordered_product.get_total_op() for ordered_product in self.ordered_products.all())
    
    def get_ordered_products(self):
        return self.ordered_products.all()


class OrderedProduct(models.Model):
    """ Products from the priceList (instance of the PricedProduct) that are selected by User to his Order:
        cannot delete the product if it already was selected to be in the order;
        default amount is 1 product of the type when the product is selected;
        if order is deleted - all ordered products for this order are deleted 
        """
    product = models.ForeignKey(Product, related_name = 'ordered', on_delete = models.PROTECT);
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0);
    quantity = models.PositiveSmallIntegerField(default = 1);
    order = models.ForeignKey(Order, related_name='ordered_products', on_delete = models.CASCADE);
    
    class Meta:
        unique_together = ('product', 'order')
        
    def get_total_op(self):
         return self.quantity * self.product.price

    

