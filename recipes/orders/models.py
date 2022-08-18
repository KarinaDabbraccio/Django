from django.db import models
from products.models import Product
from inventory.models import Location
from django.contrib.auth.models import User
    
class Order(models.Model):
    """Customer is a user who placed this order;
        User may not be deleted if he has orders;
        Consider all orders are paid before submission, 
        but this feature is not implemented.
        paid_amount = order.get_total * user.profile.user_discount
        picked_up : user picked up their order from the location
    """
    #name = models.CharField(max_length=100)
    #email = models.EmailField()
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(Location, related_name = 'orders', on_delete = models.PROTECT);
    date_ordered = models.DateTimeField(auto_now_add=True)
    picked_up = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0);
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

    

