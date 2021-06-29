from django import template

# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/


register = template.Library()


@register.filter(name="cut")
def cutt(value, arg):
    return value.replace(arg, "")
