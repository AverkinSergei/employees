from typing import Dict, List, Union

from logic.department import DepartmentEntity
from logic.employee import EmployeeEntity, PositionEntity

from employees.models import Employee
from .base import EntityNotFound, RepositoryAbc


class EmployeeRepository(RepositoryAbc):
    model = Employee

    @staticmethod
    def _entity_from_django_model(obj: Employee) -> EmployeeEntity:
        position = PositionEntity(name=obj.position.name)
        department = DepartmentEntity(name=obj.department.name, parent=obj.department.parent)
        return EmployeeEntity(
            fio=obj.fio,
            position=position,
            joined_date=obj.joined_date,
            salary=obj.salary,
            department=department,
        )

    def retrieve(self, entity_id: int, *args, **kwargs) -> Union[EmployeeEntity, EntityNotFound]:
        try:
            obj = self.model.objects.get(id=entity_id)
        except EmployeeEntity.DoesNotExists:
            raise EntityNotFound
        else:
            return self._entity_from_django_model(obj)

    def get_list(self, entity_filter: Dict = None, *args, **kwargs) -> List[EmployeeEntity]:
        if entity_filter:
            objs = self.model.objects.filter(**entity_filter).select_related(
                "department", "position"
            )
        else:
            objs = self.model.objects.all().select_related("department", "position")
        return [self._entity_from_django_model(obj) for obj in objs]
