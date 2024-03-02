from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'updated_on')