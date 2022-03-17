# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post

    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-pk'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Post
    # Используем другой шаблон — one_news.html
    template_name = 'one_news.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'one_news'



class SearchPost(PostList):
    template_name = 'search_post.html'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'one_news'