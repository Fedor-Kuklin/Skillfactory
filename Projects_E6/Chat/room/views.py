from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import RoomCreateForm
from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class RoomCreate(LoginRequiredMixin, CreateView):
    template_name = 'room/room_create.html'
    form_class = RoomCreateForm

    def form_valid(self, form):

        form.save()
        return redirect('rooms')


class RoomDelete(LoginRequiredMixin, DeleteView):
    template_name = 'room/room_delete.html'
    queryset = Room.objects.all()
    success_url = '/rooms/'
    context_object_name = 'rooms'


class RoomUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'room/room_create.html'
    form_class = RoomCreateForm
    success_url = '/rooms/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Room.objects.get(pk=id)

