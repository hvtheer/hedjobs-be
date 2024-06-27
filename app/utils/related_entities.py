def create_related_entities(
    entity_id, entity_id_attr, related_data_to_create, related_repository
):
    entities = []
    for data in related_data_to_create:
        data[entity_id_attr] = entity_id
        related_entity = related_repository.create(data)
        entities.append(related_entity)
    return entities


def delete_related_entities(
    related_data_to_delete, related_repository, related_model, related_id_attr
):
    for data in related_data_to_delete:
        condition = getattr(related_model, related_id_attr) == getattr(
            data, related_id_attr
        )
        related_repository.delete_by_condition(condition)


def update_related_entities(
    entity_id,
    entity_id_attr,
    related_data,
    related_repository,
    related_model,
    related_id_attr,
):
    # Get existing related data by entity id attribute like job_id
    existing_related_data = related_repository.get_all(
        condition=getattr(related_model, entity_id_attr) == entity_id
    )
    delete_related_entities(
        existing_related_data, related_repository, related_model, related_id_attr
    )
    created_data = create_related_entities(
        entity_id, entity_id_attr, related_data, related_repository
    )

    return created_data


# def update_related_entities(
#     entity_id,
#     entity_id_attr,
#     related_data_to_update,
#     related_repository,
#     related_model,
#     related_id_attr,
# ):
#     entities = []
#     for data in related_data_to_update:
#         data[entity_id_attr] = entity_id
#         condition = getattr(related_model, related_id_attr) == data[related_id_attr]
#         related_entity = related_repository.update_by_condition(condition, data)
#         entities.append(related_entity)
#     return entities


# def delete_create_related_entities(
#     entity_id,
#     entity_id_attr,
#     related_data,
#     related_repository,
#     related_model,
#     related_id_attr,
# ):
#     # Get existing related data by entity id attribute like job_id
#     existing_related_data = related_repository.get_all(
#         condition=getattr(related_model, entity_id_attr) == entity_id
#     )
#     # Initialize lists for data to create, update, and delete
#     data_to_create = []
#     data_to_update = []
#     data_to_delete = []

#     # Mapping of related_id_attr values to related data dictionaries for quick lookup
#     related_data_map = {data[related_id_attr]: data for data in related_data}

#     # Check for data to create or update
#     for data_dict in related_data:
#         if any(
#             getattr(existing_data, related_id_attr) == data_dict[related_id_attr]
#             for existing_data in existing_related_data
#         ):
#             # If the related_id_attr matches, add to update list
#             data_to_update.append(data_dict)
#         else:
#             # If the related_id_attr does not match any existing data, add to create list
#             data_to_create.append(data_dict)

#     # Check for data to delete
#     for existing_data in existing_related_data:
#         if getattr(existing_data, related_id_attr) not in related_data_map:
#             # If the existing data's related_id_attr is not in the provided related data, add to delete list
#             data_to_delete.append(existing_data)

#     created_data = create_related_entities(
#         entity_id, entity_id_attr, data_to_create, related_repository
#     )
#     print("created_data", related_model, created_data)
#     updated_data = update_related_entities(
#         entity_id,
#         entity_id_attr,
#         data_to_update,
#         related_repository,
#         related_model,
#         related_id_attr,
#     )
#     print("updated_data", related_model, updated_data)
#     print("data_to_delete", related_model, data_to_delete)
#     delete_related_entities(
#         data_to_delete, related_repository, related_model, related_id_attr
#     )

#     return data_to_create + data_to_update
