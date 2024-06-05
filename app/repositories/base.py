from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, instance):
        try:
            self.session.add(instance)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, instance):
        try:
            instance.is_deleted = True
            self.save(instance)
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_query(self, model):
        return self.session.query(model).filter(model.is_deleted == False)

    def get_all(self, model, condition=None):
        query = self.get_query(model)
        if condition is not None:
            query = query.filter(condition)
        return query.all()

    def get_by_id(self, model, id):
        return self.get_query(model).filter(model.id == id).first()
    
    def get_by_condition(self, model, condition):
        return self.get_query(model).filter(condition).all()

    def update_by_condition(self, model, condition, updates):
        instances = self.get_by_condition(model, condition)
        for instance in instances:
            for key, value in updates.items():
                setattr(instance, key, value)
            self.save(instance)
        return instances

    def update_by_id(self, model, id, updates):
        instance = self.get_by_id(model, id)
        if instance:
            for key, value in updates.items():
                setattr(instance, key, value)
            self.save(instance)
        return instance

    def count(self, model):
        return self.get_query(model).count()