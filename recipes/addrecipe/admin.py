from django.contrib import admin


# Register your models here.
from .models import Category, Recipe, Comment
from products.models import Group, Product, Order, OrderedProduct


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)

#from Products app:
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'price', 'available', 'weight', 'description', 'pic']
    list_filter = ['available', 'group']
    list_editable = ['price', 'available', 'weight', 'description', 'pic']
admin.site.register(Product, ProductAdmin)

admin.site.register(Group)


class OrderedProductInline(admin.TabularInline):
    model = OrderedProduct
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'created', 'inProduction', 'paid', Order.get_total]
    list_filter = ['paid', 'inProduction', 'email', 'created']
    list_editable = ['paid', 'inProduction']
    inlines = [OrderedProductInline]
admin.site.register(Order, OrderAdmin)

