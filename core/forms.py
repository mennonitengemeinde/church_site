from django.forms import ModelForm

TEXTAREA_FIELD_TYPES = ("Textarea",)
INPUT_FIELD_TYPES = (
    "TextInput",
    "URLInput",
    "EmailInput",
    "NumberInput",
    "PasswordInput",
    "DateTimeInput",
)
SELECT_FIELD_TYPES = ("Select", "LazySelect", "SelectMultiple")
FILE_WIDGET_TYPES = ("ClearableFileInput", "FileInput")
CHECKBOX_FIELD_TYPES = ("CheckboxInput", "CheckboxSelectMultiple")


class CoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     print(self.fields[field].widget.__class__.__name__)
        self.style_fields()

    def style_fields(self):
        for field in self.fields:
            style_class = ""
            if self.fields[field].widget.__class__.__name__ in INPUT_FIELD_TYPES:
                style_class = "input input-bordered w-full max-w-xs"
            elif self.fields[field].widget.__class__.__name__ in TEXTAREA_FIELD_TYPES:
                style_class = "textarea textarea-bordered w-full h-20 max-w-xs"
            elif self.fields[field].widget.__class__.__name__ in SELECT_FIELD_TYPES:
                style_class = "select select-bordered w-full max-w-xs"
            elif self.fields[field].widget.__class__.__name__ in FILE_WIDGET_TYPES:
                style_class = "file-input"
            elif self.fields[field].widget.__class__.__name__ in CHECKBOX_FIELD_TYPES:
                style_class = "toggle toggle-primary"
            self.fields[field].widget.attrs.update({"class": style_class})
