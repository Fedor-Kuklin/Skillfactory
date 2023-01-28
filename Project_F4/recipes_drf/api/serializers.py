from . import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('title',)


class RecipesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipes
        fields = ('id', 'title', 'category',  'description',)
