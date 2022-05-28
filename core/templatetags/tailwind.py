from django import template

register = template.Library()


@register.filter(name='tailwind_input')
def tailwind_input(value):
    print(value)
    return value.as_widget(attrs={'class': 'tailwind-input'})


@register.filter(name='tailwind_input_label')
def tailwind_input_label(value):
    print(value)
    return value.as_tag(attrs={'class': 'tailwind-input-label'})
