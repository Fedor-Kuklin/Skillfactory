from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Ad, Comment
from .forms import AdUpdateForm, AdCreateForm, CommentForm
from .filters import AdFilter, CommentFilter


class AdList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ad
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'board/ad.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'ad'
    paginate_by = 10


# class CommentList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Comment
#
#     # Поле, которое будет использоваться для сортировки объектов
#     ordering = '-pk'
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'board/comment.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'comment'
#     paginate_by = 10


class AdDetail(DetailView):

    queryset = Ad.objects.all()
    template_name = 'board/one_ad.html'
    context_object_name = 'one_ad'
    form = CommentForm
    extra_context = {'form': CommentForm}

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.commentAd_id = self.kwargs.get('pk')
            form.instance.commentUser = self.request.user
            form.save()

            return redirect(request.META.get('HTTP_REFERER'))


class AdCreate(LoginRequiredMixin, CreateView):
    template_name = 'board/ad_create.html'
    form_class = AdCreateForm
    permission_required = ('ad_create',)

    def form_valid(self, form):
        # Автозаполнение поля user
        form.instance.author = self.request.user
        form.save()
        return redirect('ad')


class AdUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'board/ad_update.html'
    form_class = AdUpdateForm
    login_url = reverse_lazy('ad')
    permission_required = ('ad_update',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)


class AdSearch(ListView):

    model = Ad
    template_name = 'board/ad_search.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CommentList(LoginRequiredMixin, ListView):

    template_name = 'board/user_comment.html'
    context_object_name = 'comments'
    permission_required = ('comment',)

    def get_queryset(self, **kwargs):

        user_id = self.request.user.id
        return Comment.objects.filter(commentAd__author=user_id).filter(status_remove=False).filter(status_add=False)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context['filter'] = CommentFilter(self.request.GET, queryset=self.get_queryset())
        context['new_response'] = Comment.objects. \
            filter(commentAd__author=user_id).filter(status_remove=False).filter(status_add=False)
        context['del_response'] = Comment.objects.filter(commentAd__author=user_id).filter(status_remove=True)
        context['add_response'] = Comment.objects.filter(commentAd__author=user_id).filter(status_add=True)
        return context


class CommentAccept(LoginRequiredMixin, View):
    permission_required = ('accept',)

    def get(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        comm = Comment.objects.get(pk=pk)
        comm.status_add = 1
        comm.status_del = 0
        comm.save()

        return redirect('comment')


class CommentRemove(LoginRequiredMixin, View):
    permission_required = ('remove',)

    def get(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        comm = Comment.objects.get(id=pk)
        comm.status_del = 1
        comm.status_add = 0
        comm.save()

        return redirect('comment')


