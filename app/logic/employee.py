from datetime import date
from decimal import Decimal
from typing import Dict

from .base import Entity
from .department import DepartmentEntity


class PositionEntity(Entity):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name


class EmployeeEntity(Entity):
    def __init__(
        self,
        fio: str,
        position: PositionEntity,
        joined_date: date,
        salary: Decimal,
        department: DepartmentEntity,
    ):
        self._fio = fio
        self._position = position
        self._joined_date = joined_date
        self._salary = salary
        self._department = department

    @property
    def fio(self):
        return self._fio

    @property
    def position(self):
        return self.position

    @property
    def joined_date(self):
        return self.joined_date

    @property
    def salary(self):
        return self.salary

    @property
    def department(self):
        return self.department

    def to_dict(self) -> Dict:
        return {
            "fio": self.fio,
            "position": self.position.name,
            "joined_date": self.joined_date.strftime("%d.%m.%Y %H:%I%S"),
            "salary": self.salary,
            "department": self.department.name,
        }
