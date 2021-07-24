from django.db.models import Q, QuerySet

from accounts.models import User


def get_users_from_same_church(user: User) -> QuerySet[User]:
    if user.is_superuser:
        print('running is_super')
        return User.objects.all()
    else:
        print(user.churches.all())
        return User.objects.filter(Q(churches__in=user.churches.all()) | Q(churches__isnull=True)).distinct()
