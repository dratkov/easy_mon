from django import template

register = template.Library()


@register.simple_tag
def main_menu_active(request, page_id):
    print request.path
    print page_id
    if len(request.path.split("/")) > 2 and int(page_id) == int(request.path.split("/")[2]):
        return 'active current'
    return ''
