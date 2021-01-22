from django.forms import ModelForm, HiddenInput

from contactus.models import ContactMessage


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('page_title', 'name', 'email', 'phone_number', 'message')
        widgets = {
            'page_title': HiddenInput()
        }
