from django.forms import ModelForm, HiddenInput

from contactus.models import ContactMessage


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('page_title', 'name', 'email', 'phone_number', 'message')
        widgets = {
            'page_title': HiddenInput()
        }

    def is_valid(self):
        valid = super(ContactUsForm, self).is_valid()
        if valid:
            print('is valid')
        else:
            print('not valid')
        return valid
