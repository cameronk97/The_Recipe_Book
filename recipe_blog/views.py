from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def recipe_page(request):
    return render(request, 'recipe_page.html')


def post_recipe(request):
    return render(request, 'post_recipe.html')


def edit_recipe(request):
    return render(request, 'edit_recipe.html')


def profile(request):
    return render(request, 'profile.html')


def saved_recipes(request):
    return render(request, 'saved_recipes.html')