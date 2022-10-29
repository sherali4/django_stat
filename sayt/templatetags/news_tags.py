from django import template
from sayt.models import Category

register = template.Library()

# @register.simple_tag()
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()
@register.inclusion_tag('sayt/list_categories.html')
def show_categories():
    categoriesa= Category.objects.all()
    return { "categoriesa": categoriesa }