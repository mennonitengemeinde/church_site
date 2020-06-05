from django import template

register = template.Library()


@register.filter(name='modulus')
def modulus(value, arg):
    return int(value) % int(arg)
