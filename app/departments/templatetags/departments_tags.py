from django import template

register = template.Library()


@register.inclusion_tag("tags/department_render.html")
def departments_render_department(obj):
    return {"obj": obj}
