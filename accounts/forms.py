from allauth.account.forms import SignupForm as ASignUpForm
from allauth.socialaccount.forms import SignupForm as SaSignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django_countries.fields import CountryField


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email', 'member', 'groups', 'user_permissions', 'is_superuser',
            'is_staff', 'is_active', 'date_joined', 'last_login'
        )


class MgSignupForm(ASignUpForm):
    country = CountryField().formfield()

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MgSignupForm, self).save(request)

        user.country = self.cleaned_data['country']
        user.save()

        # You must return the original result.
        return user


class SMgSignupForm(SaSignUpForm):
    country = CountryField().formfield()

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(SMgSignupForm, self).save(request)

        user.country = self.cleaned_data['country']
        user.save()

        # You must return the original result.
        return user
