from django.contrib import admin


# Register your models here.
from .models import Category
from .models import Recipe
from .models import Comment


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
