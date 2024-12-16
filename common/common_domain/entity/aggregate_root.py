from abc import ABC, abstractmethod
from common.common_domain.entity.base_entity import BaseEntity

class AggregateRoot(BaseEntity, ABC):
    @abstractmethod
    def get_id(self):
        return self._id