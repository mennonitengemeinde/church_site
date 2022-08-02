from django.forms import ModelForm, Form

TEXTAREA_FIELD_TYPES = ('Textarea',)
INPUT_FIELD_TYPES = ('TextInput', 'URLInput', 'EmailInput', 'NumberInput', 'PasswordInput', 'DateTimeInput')
SELECT_FIELD_TYPES = ('Select', 'LazySelect', 'SelectMultiple')
FILE_WIDGET_TYPES = ('ClearableFileInput', 'FileInput')
CHECKBOX_FIELD_TYPES = ('CheckboxInput', 'CheckboxSelectMultiple')


class CoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(self.fields[field].widget.__class__.__name__)
        self.style_fields()

    def style_fields(self):
        for field in self.fields:
            if self.fields[field].widget.__class__.__name__ in INPUT_FIELD_TYPES:
                self.style_widgets_input(field)
            elif self.fields[field].widget.__class__.__name__ in TEXTAREA_FIELD_TYPES:
                self.style_widgets_textarea(field)
            elif self.fields[field].widget.__class__.__name__ in SELECT_FIELD_TYPES:
                self.style_widgets_select(field)
            elif self.fields[field].widget.__class__.__name__ in FILE_WIDGET_TYPES:
                self.style_widgets_file(field)
            elif self.fields[field].widget.__class__.__name__ in CHECKBOX_FIELD_TYPES:
                self.style_widgets_checkbox(field)

    def style_widgets_input(self, field):
        self.fields[field].widget.attrs.update({'class': 'input input-bordered w-full max-w-xs'})

    def style_widgets_textarea(self, field):
        self.fields[field].widget.attrs.update({'class': 'textarea textarea-bordered w-full h-20 max-w-xs'})

    def style_widgets_select(self, field):
        self.fields[field].widget.attrs.update({'class': 'select select-bordered w-full max-w-xs'})

    def style_widgets_file(self, field):
        self.fields[field].widget.attrs.update({'class': 'file-input'})

    def style_widgets_checkbox(self, field):
        self.fields[field].widget.attrs.update({'class': 'toggle toggle-primary'})
