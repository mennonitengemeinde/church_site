from allauth.account.forms import SignupForm as ASignUpForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SaSignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.forms import CharField
from django_countries.fields import CountryField


# class MgLoginForm(LoginForm):
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.fields["login"].widget.attrs["class"] = "tailwind-input"
#     self.fields["password"].widget.attrs["class"] = "tailwind-input"
#     self.fields["remember"].widget.attrs["class"] = "tailwind-checkbox"


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email', 'churches', 'groups', 'is_superuser',
            'is_staff', 'is_active', 'date_joined', 'last_login'
        )


class MgSignupForm(ASignUpForm):
    """
    Used for Django AllAuth
    """
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=150)
    country = CountryField().formfield()

    def save(self, request):
        user = super(MgSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.save()

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
