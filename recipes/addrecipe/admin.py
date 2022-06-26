from django.contrib import admin


# Register your models here.
from .models import Category, Recipe, Comment
from products.models import Group, Product
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
#admin.site.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'sell_by', 'registered_at', 'cost']
    list_editable = ['amount', 'sell_by', 'cost']
admin.site.register(InventoryItem, InventoryItemAdmin)

class LossInventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'cost']
admin.site.register(LossInventory, LossInventoryAdmin)


#admin.site.register(LossInventory)


#from Products app:
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'price',  'weight', 'description', 'pic']
    list_filter = ['group']
    list_editable = ['price', 'weight', 'description', 'pic']
admin.site.register(Product, ProductAdmin)

admin.site.register(Group)

class OrderedProductInline(admin.TabularInline):
    model = OrderedProduct
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'created', 'shipped', 'paid', 'inventory_total_cost', Order.get_total]
    list_filter = ['paid', 'shipped', 'email']
    list_editable = ['paid', 'shipped']
    inlines = [OrderedProductInline]
admin.site.register(Order, OrderAdmin)

