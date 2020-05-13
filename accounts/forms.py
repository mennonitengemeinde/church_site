from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email', 'member', 'groups', 'user_permissions', 'is_superuser',
            'is_staff', 'is_active', 'date_joined', 'last_login'
        )
