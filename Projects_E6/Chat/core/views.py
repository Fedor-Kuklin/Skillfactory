from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.models import User

from .forms import SignUpForm, ProfileForm, UpdateUserForm, UpdateProfileForm
from .models import Profile


def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'core/user_profile.html'
#
#     # context_object_name = 'user'
#
#
#     def get_context_data(self, *args, **kwargs):
#         user = get_object_or_404(User, pk=self.kwargs.get('pk'))
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#
#         return context
#
#
# class CreateProfilePageView(CreateView):
#     template_name = 'core/create_profile.html'
#     form_class = ProfileForm
#
#     def form_valid(self, form):
#         # Автозаполнение поля user
#         form.instance.user = self.request.user.username
#         form.save()
#         return redirect('rooms')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'core/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class UserList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = User

    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'pk'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'core/users.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'users'
    # paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['profile'] = Profile.objects.all()
        # sub = list(Mail.objects.filter(subscribers=self.request.user.id).values('category'))
        # context['subscribed'] = [s['category'] for s in sub]

        return context


