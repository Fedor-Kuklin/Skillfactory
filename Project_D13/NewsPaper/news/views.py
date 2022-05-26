# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post, Category, Mail
from .filters import PostFilter
from .forms import PostForm, UserForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

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


class CategoryList(ListView):
    model = Post
    template_name = 'category.html'
    context_object_name = 'category'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Post.objects.filter(postCategory__id=self.kwargs['pk'])
        context['category'] = qs
        context['category_name'] = Category.objects.get(id=self.kwargs['pk'])
        sub = list(Mail.objects.filter(subscribers=self.request.user.id).values('category'))
        context['subscribed'] = [s['category'] for s in sub]

        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости

    queryset = Post.objects.all()
    # Используем другой шаблон — one_news.html
    template_name = 'one_news.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'one_news'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'news-{self.kwargs["pk"]}', None)
        logger.debug('fffffffffffffff')
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'news-{self.kwargs["pk"]}', obj)

        return obj



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


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('news.add_post')


# дженерик для редактирования объекта
class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('news.change_post')

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления новости
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'one_news'
    permission_required = ('news.delete_post')


class UserList(PermissionRequiredMixin, ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = User

    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'pk'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'users.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'author'
    # paginate_by = 10
    permission_required = ('auth.view_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_id = Group.objects.get(name='authors')
        context['users_in_authors'] = User.objects.filter(groups=group_id.id)
        # sub = list(Mail.objects.filter(subscribers=self.request.user.id).values('category'))
        # context['subscribed'] = [s['category'] for s in sub]

        return context


class UserDetail(PermissionRequiredMixin, DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = User

    template_name = 'user.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'user'
    permission_required = ('auth.view_user')


class UserCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'user_create.html'
    form_class = UserForm
    permission_required = ('auth.change_user')


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'user_create.html'
    form_class = UserForm
    permission_required = ('auth.change_user')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)

    success_url = '/news/author/'


@login_required
def add_subscribe(request, pk):
    user = request.user
    if not Mail.objects.filter(subscribers=get_user_model().objects.get(id=user.id),
                               category=Category.objects.get(id=pk)).exists():
        Mail.objects.create(subscribers=get_user_model().objects.get(id=user.id),
                            category=Category.objects.get(id=pk))

    return redirect('/news/')

@login_required
def remove_subscribe(request, pk):
    user = request.user

    if Mail.objects.filter(subscribers=get_user_model().objects.get(id=user.id),
                           category=Category.objects.get(id=pk)).exists():
        Mail.objects.filter(subscribers=get_user_model().objects.get(id=user.id),
                            category=Category.objects.get(id=pk)).delete()


    return redirect('/news/')
