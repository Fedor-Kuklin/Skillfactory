from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/signup_success/'


class SignupSuccessView(TemplateView):
     template_name = 'sign/signup_success.html'



@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    # author = Author.objects.get(name='User')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
        # if not request.user.groups.filter(name='User').exists():
        #     author.user_set.add(user)


    return redirect('/')


