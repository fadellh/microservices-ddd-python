from abc import ABC, abstractmethod


class BaseEntity(ABC):
    def __init__(self, entity_id):
        self._id = entity_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, entity_id):
        self._id = entity_id

    @abstractmethod
    def get_id(self):
        pass