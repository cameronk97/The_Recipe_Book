from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/', views.recipe_page, name='recipe_page'),
    path('post/', views.post_recipe, name='post_recipe'),
    path('edit/', views.edit_recipe, name='edit_recipe'),
    path('profile/', views.profile, name='profile'),
    path('saved/', views.saved_recipes, name='saved_recipes'),
]
