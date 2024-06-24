from sqlalchemy import Column, DateTime, Boolean, func
from sqlalchemy.orm import as_declarative, declared_attr

@as_declarative()
class Base:
    __abstract__ = True

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=func.now(), onupdate=func.now())
