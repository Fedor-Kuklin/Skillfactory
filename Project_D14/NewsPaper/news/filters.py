from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, PostCategory





# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о новости
    class Meta:
        model = Post

        fields = {
            'dateCreation': ['gt', 'lt'],
            'title': ['icontains'],
            # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author__authorUser__username': ['icontains'],  # количество должно быть больше или равно тому, что указал пользователь

        }

