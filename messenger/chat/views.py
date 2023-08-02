from django.views.generic import ListView, CreateView

from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User


class UserList(ListView):
    model = User
    ordering = 'username'
    template_name = 'users.html'
    context_object_name = 'users'


class ProfileCreate(CreateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profile_edit.html'
