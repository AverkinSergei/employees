from django.contrib.admin import ModelAdmin, register

from .models import Employee


@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ["fio", "department"]
    search_fields = ["fio", "position"]
    list_filter = ["position", "department"]
    ordering = ["department", "position", "fio"]
