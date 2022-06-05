from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    """ The name field has to be unique, so to avoid duplicates. 
        The description is just to give a hint of what the category is all about.
        Has zero or many Recipes.
        Created by admin only.
        """   
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    """ May be associated with only one Category, which is not null.
        Has only one User - author.
        The related_name parameter will be used to create a reverse relationship 
        where the Category instances will have access a list of Recipe instances 
        that belong to it.
        """
    subject = models.CharField(max_length=100)
    cooking_time = models.IntegerField();
    rec_description = models.CharField(max_length=1000)
    last_updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)


class Comment(models.Model):
    """ Must have one, and only one User associated with: created_by.
        Set the current date and time when a Comment is created.
        The updated_by field sets the related_name='+' - we don’t need this 
        reverse relationship, so it will be ignored.
        """
    message = models.TextField(max_length=4000)
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)