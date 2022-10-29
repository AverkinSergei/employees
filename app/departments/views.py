from django.shortcuts import render

from .models import Department


def departments_tree(request):
    obj_list = Department.objects.all().prefetch_related("staff")
    context = {
        "obj_list": obj_list,
    }
    return render(request, "employee_tree.html", context=context)
