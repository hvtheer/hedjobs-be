from fastapi import status
from app.config.constants import ErrorMessage, SuccessMessage
from .search import *
from .exception import CustomException


def create_related_entities(
    entity_id, entity_id_attr, related_data_to_create, related_repository
):
    entities = []
    for data in related_data_to_create:
        data[entity_id_attr] = entity_id
        related_entity = related_repository.create(data)
        entities.append(related_entity)
    return entities


def update_related_entities(
    entity_id,
    entity_id_attr,
    related_data_to_update,
    related_repository,
    related_model,
    related_id_attr,
):
    entities = []
    for data in related_data_to_update:
        data[entity_id_attr] = entity_id
        condition = getattr(related_model, related_id_attr) == data[related_id_attr]
        related_entity = related_repository.update_by_condition(condition, data)
        entities.append(related_entity)
    return entities


# def delete_related_entities(
#     related_data_to_delete,
#     related_repository,
#     related_model,
#     related_id_attr,
# ):
#     for data in related_data_to_delete:
#         condition = getattr(related_model, related_id_attr) == getattr(
#             data, related_id_attr
#         )
#         related_repository.delete_by_condition(condition)


def delete_related_entities(
    related_data_to_delete, related_repository, related_model, related_id_attr
):
    for data in related_data_to_delete:
        condition = getattr(related_model, related_id_attr) == getattr(
            data, related_id_attr
        )
        related_repository.delete_by_condition(condition)


def create_user_role_entity(user, role, repository):
    if user.role == role:
        new_entity = {
            f"{role.lower()}_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "phone_number": user.phone_number,
        }
        repository.create(new_entity)


def get_record_or_404(
    repository,
    condition,
    error_message=ErrorMessage.NOT_FOUND,
    status_code=status.HTTP_404_NOT_FOUND,
):
    record = repository.get_first_by_condition(condition)
    if not record:
        raise CustomException(status_code=status_code, detail=error_message)
    return record


def ensure_unique_record(
    repository,
    condition,
    error_message=ErrorMessage.ALREADY_EXISTS,
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
):
    if repository.get_first_by_condition(condition):
        raise CustomException(status_code=status_code, detail=error_message)
