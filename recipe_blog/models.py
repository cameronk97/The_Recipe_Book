from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField
    instructions = models.TextField
    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    saves = models.ManyToManyField(User, related_name='recipe_saves', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.id)

    def number_of_saves(self):
        return self.saves.count()


class SavedRecipes(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="saved_recipes")
    user = models.ManyToManyField(User, blank=True)