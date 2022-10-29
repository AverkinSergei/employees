from typing import Dict, List, Union

from departments.models import Department
from logic.department import DepartmentEntity
from logic.employee import EmployeeEntity

from .base import EntityNotFound, RepositoryAbc


class DepartmentRepository(RepositoryAbc):
    model = Department

    def _entity_from_django_model(self, obj: Department) -> DepartmentEntity:
        try:
            parent = Department(
                name=obj.parent.name, parent=self._entity_from_django_model(obj.parent)
            )
        except RecursionError:
            parent = None
        return DepartmentEntity(name=obj.name, parent=parent)

    def retrieve(self, entity_id: int, *args, **kwargs) -> Union[DepartmentEntity, EntityNotFound]:
        try:
            obj = self.model.objects.get(id=entity_id)
        except EmployeeEntity.DoesNotExists:
            raise EntityNotFound
        else:
            return self._entity_from_django_model(obj)

    def get_list(self, entity_filter: Dict = None, *args, **kwargs) -> List[DepartmentEntity]:
        if entity_filter:
            objs = self.model.objects.filter(**entity_filter).select_related("staff", "parent")
        else:
            objs = self.model.objects.all().select_related("staff", "parent")
        return [self._entity_from_django_model(obj) for obj in objs]
