from django import template
import math

register = template.Library()


@register.filter(name='ceil')
def ceil(value):
    return math.ceil(value)
