from accounts.models import User
from churches.models import Church


def get_member_churches(user: User):
    return Church.objects.filter(members=user)
