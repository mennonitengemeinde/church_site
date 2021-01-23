from django.db import models


class ChurchManager(models.Manager):

    def get_member_churches(self, user):
        return self.filter(members=user)
