from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')


admin.site.register(models.Recipes, RecipeAdmin)
