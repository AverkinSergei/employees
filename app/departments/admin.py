from django.contrib.admin import register
from mptt.admin import DraggableMPTTAdmin

from .models import Department


@register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    list_display = [
        "indented_title",
        "name",
    ]

    def get_queryset(self, request, **kwargs):
        qs = super().get_queryset(request)
        return qs.prefetch_related("staff")
