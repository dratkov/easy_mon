from django import template
register = template.Library()


@register.filter
def split(str, splitter):
        return str.split(splitter)


@register.filter
def replace(value, arg):
            arg1 = arg.split(", ")[0]
            arg2 = arg.split(", ")[1]
            return value.replace(arg1, arg2)
