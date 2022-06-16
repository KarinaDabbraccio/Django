from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import category_recipes
from ..models import Category

       
        
class CategoryResipesTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Testing', description='Testing category.')

    def test_category_recipes_view_success_status_code(self):
        url = reverse('addrecipe:category_recipes', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_recipes_view_not_found_status_code(self):
        url = reverse('addrecipe:category_recipes', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_category_recipes_url_resolves_category_recipes_view(self):
        view = resolve('/addrecipe/1/')
        self.assertEquals(view.func, category_recipes)
        
   # def test_category_recipes_view_contains_navigation_links(self):
    #    category_recipes_url = reverse('addrecipe:category_recipes', kwargs={'pk': 1})
     #   addrecipe_url = reverse('addrecipe:addrecipe')
      #  new_recipe_url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})

       # response = self.client.get(category_recipes_url)

        #self.assertContains(response, 'href="{0}"'.format(addrecipe_url))
        #self.assertContains(response, 'href="{0}"'.format(new_recipe_url))
    
