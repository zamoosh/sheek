from django import template
import os
from django.conf import settings

register = template.Library()


@register.simple_tag
def version(debug=None):
    """Removes all values of arg from the given string"""
    if settings.DEBUG == False and debug:
        return "-" + os.environ.get("VERSION")
    elif settings.DEBUG == True and debug:
        return ''
    if os.environ.get("VERSION"):
        return os.environ.get("VERSION")
    else:
        return 'local'