from datetime import datetime, timedelta
from django.forms import HiddenInput, DateTimeField
from django.utils import timezone

from contactus.models import ContactMessage
from core.forms import CoreModelForm


class ContactUsForm(CoreModelForm):
    form_no = DateTimeField(widget=HiddenInput(), initial=timezone.now)

    class Meta:
        model = ContactMessage
        fields = ('page_title', 'name', 'email', 'phone_number', 'message')
        widgets = {
            'page_title': HiddenInput(),
        }

    def save(self, commit=False):
        form_no_plus_five = datetime.strptime(self.data['form_no'],
                                              '%Y-%m-%d %H:%M:%S.%f') + timedelta(seconds=5)
        if self.cleaned_data['form_no'] is None or form_no_plus_five > datetime.now():
            return super().save(commit=False)
        return super().save(commit=True)
