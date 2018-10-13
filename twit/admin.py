from django.contrib import admin

from twit.models import Message, Follow

admin.site.register(Message)
admin.site.register(Follow)
