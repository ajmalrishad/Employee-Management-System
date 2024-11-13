from django import template

register = template.Library()

@register.filter
def get_field(custom_fields, field_name):
    return custom_fields.get(field_name, '')
