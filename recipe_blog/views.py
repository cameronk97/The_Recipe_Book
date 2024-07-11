from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe

def home(request):
    return render(request, 'index.html')


def recipe_page(request):
    return render(request, 'recipe_page.html')

class RecipePage(View):

    def get(self, request, slug, *args, **kwargs):
            queryset = Recipe.objects.all()
            recipe = get_object_or_404(queryset, slug=slug)
            ingredients = recipe.ingredients.splitlines()
            saved = False
            if recipe.saves.filter(id=self.request.user.id).exists():
                saved = True

            return render(
                request,
                "recipe_page.html",
                {
                    "recipe": recipe,
                    "saved": saved,
                    "ingredients": ingredients
                },
            )
    
    def recipe(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        saved = False
        ingredients = [ingredient.strip() for ingredient in ingredients if ingredient.strip()]
        if recipe.saves.filter(id=self.request.user.id).exists():
            saved = True


        return render(
            request,
            "recipe_page.html",
            {
                "recipe": recipe,
                "saved": saved,
                "ingredients": ingredients
            },
        )


def post_recipe(request):
    return render(request, 'post_recipe.html')


def edit_recipe(request):
    return render(request, 'edit_recipe.html')


def profile(request):
    return render(request, 'profile.html')


def saved_recipes(request):
    return render(request, 'saved_recipes.html')

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
