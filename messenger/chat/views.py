from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .forms import ProfileForm
from .models import Profile, Chat
from django.contrib.auth.models import User


class ProfileList(ListView):
    model = Profile
    template_name = 'users.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = Profile
    template_name = 'user.html'
    context_object_name = 'user_detail'


class ChatList(ListView):
    model = Chat
    template_name = 'chats.html'
    context_object_name = 'chats'


class ChatDetail(DetailView):
    model = Chat
    template_name = 'chat.html'
    context_object_name = 'chat_detail'


class ProfileCreate(CreateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profile_edit.html'


class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('user_detail')
