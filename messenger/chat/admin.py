from django.contrib import admin

from chat.models import Profile, Chat, Messages, ChatUser

admin.site.register(Profile)
admin.site.register(Chat)
admin.site.register(Messages)
admin.site.register(ChatUser)
