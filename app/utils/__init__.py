from .search import *


def create_related_entities(entity_id, link_key, entities_data, create_method):
    """
    Utility function to create related entities like skills, certificates, educations,
    for any main entity like job, student, or company.
    """
    entities = []
    for entity_data in entities_data:
        entity_data[
            link_key
        ] = entity_id  # Use the link_key to assign the main entity's ID
        created_entity = create_method(entity_data)
        entities.append(created_entity)
    return entities


def create_user_role_entity(self, user, role, repository):
    if user.role == role:
        new_entity = {
            f"{role.lower()}_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "phone_number": user.phone_number,
        }
        repository.create(new_entity)
