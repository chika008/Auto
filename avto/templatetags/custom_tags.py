from django import template

from avto.models import Body

register = template.Library()


@register.simple_tag()
def get_categories():
    return Body.objects.all()