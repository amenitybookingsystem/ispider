from django import template

register = template.Library()

@register.filter
def create_range(start, stop):
    stop = stop + 1
    return range(start, stop)

