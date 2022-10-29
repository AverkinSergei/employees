from django.db import models
from django.utils.translation import gettext as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Department(MPTTModel):
    name = models.CharField(_("name"), max_length=60)
    parent = TreeForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
