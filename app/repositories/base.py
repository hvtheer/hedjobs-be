import logging
from sqlalchemy import Index, inspect, Column, Boolean, asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional, Type, TypeVar, Generic, Dict, Any
from fastapi import status

from app.utils.exception import CustomException
from app.config.constants import ErrorMessage

T = TypeVar("T")
logger = logging.getLogger(__name__)


class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T], column_id: Column):
        self.session = session
        self.model = model
        self.column_id = column_id
        self.column_delete = "is_deleted"

    def create(self, obj_in: dict) -> T:
        obj = self.model(**obj_in)
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in create for model {self.model.__name__}: {e}"
            )
            self.session.rollback()
            raise e

    def _filter_not_deleted(self):
        if hasattr(self.model, self.column_delete):
            return self.session.query(self.model).filter(
                getattr(self.model, self.column_delete) == False
            )
        return self.session.query(self.model)

    def get_by_id(self, id: int) -> Optional[T]:
        try:
            return self._filter_not_deleted().filter(self.column_id == id).first()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in get_by_id for model {self.model.__name__} with id {id}: {e}"
            )
            raise e

    def get_first_by_condition(self, condition=None) -> Optional[T]:
        try:
            return self._filter_not_deleted().filter(condition).first()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in get_first_by_condition for model {self.model.__name__}: {e}"
            )
            raise e

    def get_all(self, pagination: Dict[str, Any] = None, condition=None, order_by=None):
        try:
            query = self._filter_not_deleted()
            if condition is not None:
                query = query.filter(condition)
            if order_by is not None:
                # Check if order_by is a list of columns and unpack it
                if isinstance(order_by, list):
                    query = query.order_by(*order_by)
                else:
                    # Single column, maintain backward compatibility
                    query = query.order_by(order_by)
            if pagination:
                if "page" in pagination and "size" in pagination:
                    page = pagination["page"]
                    size = pagination["size"]
                    query = query.offset((page - 1) * size).limit(size)
            return query.all()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in get_all for model {self.model.__name__}: {e}"
            )
            raise e

    def update_by_id(self, id: int, obj_in: dict) -> T:
        try:
            self._filter_not_deleted().filter(self.column_id == id).update(obj_in)
            self.session.commit()
            return self._filter_not_deleted().filter(self.column_id == id).first()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in update_by_id for model {self.model.__name__} with id {id}: {e}"
            )
            self.session.rollback()
            raise e

    def update_by_condition(self, condition: dict, obj_in: dict) -> T:
        try:
            self._filter_not_deleted().filter_by(**condition).update(obj_in)
            self.session.commit()
            return self._filter_not_deleted().filter_by(**condition).first()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in update_by_condition for model {self.model.__name__} with condition {condition}: {e}"
            )
            self.session.rollback()
            raise e

    def delete_by_id(self, id: int) -> bool:
        try:
            if hasattr(self.model, self.column_delete):
                self.update_by_id(id, {self.column_delete: True})
            else:
                entity = self.get_by_id(id)
                if entity:
                    self.session.delete(entity)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in delete_by_id for model {self.model.__name__} with id {id}: {e}"
            )
            self.session.rollback()
            return False

    def delete_by_condition(self, condition) -> bool:
        try:
            if hasattr(self.model, self.column_delete):
                self.update_by_condition(condition, {self.column_delete: True})
            else:
                deleted_count = self._filter_not_deleted().filter(condition).delete()
                if deleted_count == 0:
                    return False
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in delete_by_condition for model {self.model.__name__} with condition {condition}: {e}"
            )
            self.session.rollback()
            return False

    def count(self, condition=None) -> int:
        try:
            query = self._filter_not_deleted()
            if condition is not None:
                query = query.filter(condition)
            return query.count()
        except SQLAlchemyError as e:
            logger.error(
                f"An error occurred in count for model {self.model.__name__}: {e}"
            )
            raise e
