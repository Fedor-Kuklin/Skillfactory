from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from news.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/signup_success/'


class SignupSuccessView(TemplateView):
     template_name = 'sign/signup_success.html'



@login_required
def add_authors(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')

    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
        Author.objects.create(authorUser=user)

    return redirect('/')

@login_required
def remove_authors(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')

    if request.user.groups.filter(name='authors').exists():
        premium_group.user_set.remove(user)
        Author.objects.filter(authorUser=user).delete()

    return redirect('/')
