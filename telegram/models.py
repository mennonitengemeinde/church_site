from django.db import models


class LiveSubscription(models.Model):
    chat_type = models.CharField(max_length=50)
    chat_id = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=200)
    subscription_date = models.DateTimeField(auto_now_add=True)
    language_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
