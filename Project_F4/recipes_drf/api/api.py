from rest_framework import viewsets
from .serializers import CategorySerializer, RecipesSerializer
from .models import Category, Recipes


class CategoryListAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    queryset = Category.objects.all()


class RecipesListAPIView(viewsets.ModelViewSet):
    serializer_class = RecipesSerializer

    queryset = Recipes.objects.all()
