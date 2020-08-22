from django.contrib import admin
from .models import Conversation, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created")


@admin.register(Conversation)
class Conversation(admin.ModelAdmin):
    list_display = ("__str__", "count_messages", "count_participants")
