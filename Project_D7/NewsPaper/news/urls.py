from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, UserList, PostDetail, UserDetail, SearchPost, PostCreateView, PostUpdateView, \
                     PostDeleteView, UserCreateView, UserUpdateView, CategoryList, add_subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='news'),
      # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('category/<int:pk>/', CategoryList.as_view(), name='category'),
   path('<int:pk>/subscribe/', add_subscribe, name='subscribe_category'),
   path('<int:pk>', PostDetail.as_view(), name='one_news'),
   path('create/', PostCreateView.as_view(), name='post_create'),
   path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
   path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
   path('search/', SearchPost.as_view(), name='search_post'),
   path('author/', UserList.as_view(), name='author'),
   path('author/<int:pk>', UserDetail.as_view(), name='user'),
   path('author/create/', UserCreateView.as_view(), name='user_create'),
   path('author/create/<int:pk>', UserUpdateView.as_view(), name='user_update'),
]