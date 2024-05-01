from allauth.account.forms import SignupForm as ASignUpForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SaSignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from django.forms import CharField, TextInput, Textarea, CheckboxInput, Select, ModelForm, SelectMultiple
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class MgLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["password"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email', 'churches', 'groups', 'is_superuser',
            'is_staff', 'is_active', 'date_joined', 'last_login'
        )
        widgets = {
            'username': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'first_name': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'last_name': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'email': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'churches': SelectMultiple(attrs={'class': 'select select-bordered select-multiple w-full max-w-sm'}),
            'groups': SelectMultiple(attrs={'class': 'select select-bordered select-multiple w-full max-w-sm'}),
            'is_superuser': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'is_staff': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'is_active': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
            'date_joined': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'last_login': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
        }


class MgSignupForm(ASignUpForm):
    """
    Used for Django AllAuth
    """
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=150)
    country = CountryField().formfield()
    captcha = ReCaptchaField(widget=ReCaptchaV3(action='signup'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["username"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["password1"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["password2"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["first_name"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["last_name"].widget.attrs["class"] = "input input-bordered w-full max-w-sm"
        self.fields["country"].widget.attrs["class"] = "select select-bordered w-full max-w-sm"
        # self.fields["accept_terms"].widget.attrs["class"] = "tailwind-checkbox"

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


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': TextInput(attrs={'class': 'input input-bordered w-full max-w-sm'}),
            'permissions': SelectMultiple(attrs={'class': 'select select-bordered select-multiple w-full max-w-sm'}),
        }
