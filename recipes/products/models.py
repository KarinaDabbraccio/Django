from django.db import models


class Group(models.Model):
    """ The name field has to be unique, so to avoid duplicates. 
        Has zero or many Products.
        Created by admin only.
        """   
    name = models.CharField(max_length=40, unique=True)
    pic = models.ImageField(upload_to='images/', null=True, default = 'null');

    
    def __str__(self):
        return self.name
    
    def get_products_count(self):
        return Product.objects.filter(group=self).count()


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
    price = models.DecimalField(max_digits=7, decimal_places=2);
    pic = models.ImageField(upload_to='images/', null=True, default = 'null');
    available = models.BooleanField();
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    """Customer is a user who placed this order;
    User may not be deleted if he has orders;
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    inProduction = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    
    def get_total(self):
        return sum(ordered_product.get_total_op() for ordered_product in self.ordered_products.all())

class OrderedProduct(models.Model):
    """ Products thst are selected by User to his Order:
        cannot delete the product if it already was selected to be in the order;
        default amount is 1 product of the type when the product is selected;
        if order is deleted - all ordered products for this order are deleted 
        """
    product = models.ForeignKey(Product, related_name = 'ordered', on_delete = models.PROTECT);
    price = models.DecimalField(max_digits=7, decimal_places=2, default = '0');
    quantity = models.PositiveSmallIntegerField(default = 1);
    order = models.ForeignKey(Order, related_name='ordered_products', on_delete = models.CASCADE);
    
    class Meta:
        unique_together = ('product', 'order')
        
    def get_total_op(self):
         return self.quantity * self.product.price

    

