from django.template.defaultfilters import slugify

from core.forms import CoreModelForm
from forms.models import Form, Translation


class FormCreateForm(CoreModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description', 'language', 'embed_url', 'is_active']

    def save(self, commit=False):
        form = super(FormCreateForm, self).save(commit=False)
        form.slug = slugify(form.name)
        form.save()
        return form


class TranslationCreateForm(CoreModelForm):
    class Meta:
        model = Translation
        fields = ['name', 'description', 'language', 'embed_url']
