from .search import *
from .user import *


def create_job_related_entities(job_id, entities_data, create_method):
    """
    Utility function to create job related entities like skills, certificates, and educations.
    """
    entities = []
    for entity_data in entities_data:
        entity_data["job_id"] = job_id
        created_entity = create_method(entity_data)
        entities.append(created_entity)
    return entities
