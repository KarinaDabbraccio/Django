from django.contrib import admin


# Register your models here.
from .models import Category, Recipe, Comment
from products.models import Group, Product, PricedProduct
from orders.models import Order, OrderedProduct
from accounts.models import Profile
from sales.models import SoldItem

from inventory.models import Manufacturer, Location, InventoryItem, LossInventory

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)

admin.site.register(Profile)
admin.site.register(SoldItem)

#admin.site.register(Manufacturer)
#admin.site.register(Location)
admin.site.register(InventoryItem)
admin.site.register(LossInventory)


#from Products app:
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'weight', 'description', 'pic']
    list_filter = ['group']
    list_editable = ['weight', 'description', 'pic']
admin.site.register(Product, ProductAdmin)

admin.site.register(Group)
admin.site.register(PricedProduct)


class OrderedProductInline(admin.TabularInline):
    model = OrderedProduct
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'created', 'inProduction', 'paid', Order.get_total]
    list_filter = ['paid', 'inProduction', 'email', 'created']
    list_editable = ['paid', 'inProduction']
    inlines = [OrderedProductInline]
admin.site.register(Order, OrderAdmin)

