from django.forms import ModelForm, HiddenInput, TextInput, Textarea

from contactus.models import ContactMessage


class ContactUsForm(ModelForm):
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

    def is_valid(self):
        valid = super(ContactUsForm, self).is_valid()
        if valid:
            print('is valid')
        else:
            print('not valid')
        return valid
