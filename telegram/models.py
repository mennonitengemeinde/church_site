# from django.db import models
#
#
# class TelegramUser(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     chat_id = models.BigIntegerField()
#     preferred_language = models.IntegerField(choices=(('English', 1), ('German', 2), ('Spanish', 3)))
#     bot = models.IntegerField(choices=(('WOL Events Bot', 1), ('Wol Bulletin', 2)))
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.bot} - {self.first_name}'


# class LiveSubscription(models.Model):
#     chat_type = models.CharField(max_length=50)
#     chat_id = models.CharField(unique=True, max_length=100)
#     name = models.CharField(max_length=200)
#     subscription_date = models.DateTimeField(auto_now_add=True)
#     language_code = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
