from atexit import register
from django import template



register = template.Library()

@register.filter(name="onlelinebrake")
def onlelinebrake(value):
    a = value
    b = a.split(maxsplit=1)

    c = "<br>".join(b)
    return c



@register.filter()
def multiply(value, arg):
    return float(value) * arg


