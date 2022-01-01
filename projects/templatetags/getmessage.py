from django import template
from projects.models import Message

register = template.Library()

@register.filter(name='message')
def message(value):
    messeages = Message.objects.filter(project=value.id).order_by('-created_at')
    return messeages