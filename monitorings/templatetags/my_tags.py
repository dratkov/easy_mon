from django import template

register = template.Library()


@register.simple_tag
def main_menu_active(request, href):
    if href and href in request.path:
        return 'active current'
    return ''
