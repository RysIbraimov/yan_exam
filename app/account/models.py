from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telegram_chat_id = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.user.username






