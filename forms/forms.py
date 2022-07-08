from django.forms import ModelForm, TextInput, Textarea, Select, CheckboxInput
from django.template.defaultfilters import slugify

from forms.models import Form, Translation


class FormCreateForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description', 'language', 'embed_url', 'is_active']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'input input-bordered w-full max-w-sm'}),
            'description': Textarea(
                attrs={'placeholder': 'Description', 'class': 'textarea textarea-bordered w-full h-20 max-w-sm'}),
            'language': Select(attrs={'placeholder': 'Language', 'class': 'select select-bordered w-full max-w-sm'}),
            'embed_url': TextInput(attrs={'placeholder': 'Embed URL', 'class': 'input input-bordered w-full max-w-sm'}),
            'is_active': CheckboxInput(attrs={'class': 'toggle toggle-primary'}),
        }

    def save(self, commit=False):
        form = super(FormCreateForm, self).save(commit=False)
        form.slug = slugify(form.name)
        form.save()
        return form


class TranslationCreateForm(ModelForm):
    class Meta:
        model = Translation
        fields = ['name', 'description', 'language', 'embed_url']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'input input-bordered w-full max-w-sm'}),
            'description': Textarea(
                attrs={'placeholder': 'Description', 'class': 'textarea textarea-bordered w-full h-20 max-w-sm'}),
            'language': Select(attrs={'placeholder': 'Language', 'class': 'select select-bordered w-full max-w-sm'}),
            'embed_url': TextInput(attrs={'placeholder': 'Embed URL', 'class': 'input input-bordered w-full max-w-sm'}),
        }
