from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

from app.logic.base import Entity


class EntityNotFound(Exception):
    ...


class RepositoryAbc(ABC):
    @abstractmethod
    def retrieve(self, entity_id: Any, *args, **kwargs) -> Union[Entity, EntityNotFound]:
        ...

    @abstractmethod
    def get_list(self, entity_filter: Dict = None, *args, **kwargs) -> List[Entity]:
        ...
