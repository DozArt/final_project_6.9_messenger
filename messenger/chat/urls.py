from django.urls import path
# Импортируем созданное нами представление
from .views import UserList, ProfileCreate

urlpatterns = [
   path('', UserList.as_view()),
   path('create/', ProfileCreate.as_view(), name='profile_create'),
]