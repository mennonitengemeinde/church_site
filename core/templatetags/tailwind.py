from django import template

from core.forms import INPUT_FIELD_TYPES

register = template.Library()


@register.filter(name='tailwind_input')
def tailwind_input(value):
    return value.as_widget(attrs={'class': 'input input-bordered w-full max-w-xs'})


@register.filter(name='tailwind_input_label')
def tailwind_input_label(value):
    return value.as_tag(attrs={'class': 'tailwind-input-label'})


@register.filter(name='tailwind_select')
def tailwind_select(value):
    return value.as_widget(attrs={'class': 'input input-bordered w-full max-w-xs'})
