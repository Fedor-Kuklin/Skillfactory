from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .api import CategoryListAPIView, RecipesListAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Recipes API",
      default_version='v1.0.0',
      description="API of the recipe catalog consisting of categories and recipes in these categories",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

routes = DefaultRouter()

routes.register('category', CategoryListAPIView, basename='category')
routes.register('recipes', RecipesListAPIView, basename='recipes')

urlpatterns = [
    path('', include(routes.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]