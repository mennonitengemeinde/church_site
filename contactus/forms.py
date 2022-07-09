from datetime import datetime, timedelta
from django.forms import ModelForm, HiddenInput, TextInput, Textarea, DateTimeField
from django.utils import timezone

from contactus.models import ContactMessage


class ContactUsForm(ModelForm):
    form_no = DateTimeField(widget=HiddenInput(), initial=timezone.now)

    class Meta:
        model = ContactMessage
        fields = ('page_title', 'name', 'email', 'phone_number', 'message')
        widgets = {
            'page_title': HiddenInput(),
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'input input-bordered w-full max-w-sm'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'input input-bordered w-full max-w-sm'}),
            'phone_number': TextInput(
                attrs={'placeholder': 'Phone Number', 'class': 'input input-bordered w-full max-w-sm'}),
            'message': Textarea(
                attrs={'placeholder': 'Message', 'class': 'textarea textarea-bordered h-20 w-full max-w-sm'}),
        }

    def save(self, commit=False):
        form_no_plus_five = datetime.strptime(self.data['form_no'],
                                              '%Y-%m-%d %H:%M:%S.%f') + timedelta(seconds=5)
        if self.cleaned_data['form_no'] is None or form_no_plus_five > datetime.now():
            return super().save(commit=False)
        return super().save(commit=True)
