from django.urls import path
# Импортируем созданное нами представление
from .views import ProfileList, ProfileCreate, ChatList, UserDetail, ProfileUpdate, ChatDetail

urlpatterns = [
   path('/', ProfileList.as_view(), name='messenger'),
   path('users/', ProfileList.as_view(), name='users'),
   path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
   path('users/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
   path('create/', ProfileCreate.as_view(), name='profile_create'),
   path('chats/', ChatList.as_view(), name='chat_list'),
   path('chats/<int:pk>', ChatDetail.as_view(), name='chat_detail'),
]
