from departments.models import Department
from django.db import models
from django.utils.translation import gettext as _


class Position(models.Model):
    name = models.CharField(_("name"), max_length=60)

    class Meta:
        verbose_name = _("position")
        verbose_name_plural = _("positions")


class Employee(models.Model):
    fio = models.CharField(_("fio"), max_length=100)
    position = models.ForeignKey(
        Position, on_delete=models.PROTECT, verbose_name=_("position"), related_name="employees"
    )
    joined_date = models.DateField(_("joined_date"))
    salary = models.DecimalField(_("salary"), decimal_places=2, max_digits=12)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, verbose_name=_("department"), related_name="staff"
    )

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")
