from django import template

from home.consts import CALCULATION_FIELDS

register = template.Library()


@register.filter
def in_calculation_fields(value):
    return value in CALCULATION_FIELDS
