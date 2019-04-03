from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def post_available(context, format_string):
    return datetime.now().strftime(format_string)