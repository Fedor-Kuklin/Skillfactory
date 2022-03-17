from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, SearchPost, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='one_news'),
   path('create/', PostCreateView.as_view(), name='post_create'),
   path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
   path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
   path('search/', SearchPost.as_view(), name='search_post'),
]