from typing import Type, Optional
from sqlalchemy.orm import Session
from repository.base import BaseRepository

class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_all(self, model: Type, condition=None):
        return self.repository.get_all(model, condition)

    def get_by_id(self, model: Type, id: int):
        return self.repository.get_by_id(model, id)

    def create(self, model: Type, **kwargs):
        instance = model(**kwargs)
        self.repository.save(instance)
        return instance

    def update_by_id(self, model: Type, id: int, updates: dict):
        return self.repository.update_by_id(model, id, updates)

    def delete(self, model: Type, id: int):
        instance = self.get_by_id(model, id)
        if instance:
            self.repository.delete(instance)
        return instance