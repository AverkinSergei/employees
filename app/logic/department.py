from typing import Dict, List

from .base import Entity


class DepartmentEntity(Entity):
    def __init__(self, name: str, parent: Entity = None, staff: List[Entity] = None):
        self._parent = parent
        self._name = name
        self._staff = staff

    @property
    def parent(self):
        return self._parent

    @property
    def name(self):
        return self._name

    @property
    def staff(self):
        return self._staff

    def to_dict(self) -> Dict:
        return {
            "parent": self.parent.to_dict(),
            "name": self.name,
            "staff": [emp.to_dict() for emp in self.staff],
        }
