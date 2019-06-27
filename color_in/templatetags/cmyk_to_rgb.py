from django import template
from django.template.defaultfilters import stringfilter

from math import ceil

register = template.Library()

@register.filter
@stringfilter
def to_rgb(value):
    cmyk_arr = value.split(',')
    cmyk_arr = list(map(int, cmyk_arr))

    C = cmyk_arr[0]/100
    M = cmyk_arr[1]/100
    Y = cmyk_arr[2]/100
    K = cmyk_arr[3]/100

    r =  ceil(255 * (1 - C) * (1 - K))
    g =  ceil(255 * (1 - M) * (1 - K))
    b =  ceil(255 * (1 - Y) * (1 - K))

    return ','.join(map(str, [r, g, b]))
