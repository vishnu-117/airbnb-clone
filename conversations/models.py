from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User")

    def __str__(self):
        username = []
        for user in self.participants.all():
            username.append(user.username)
        return ", ".join(username)

    def count_messages(self):
        return self.messages.count()
    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()
    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    message = models.CharField(max_length=200)
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'
