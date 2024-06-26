def create_user_role_entity(self, user, role, repository):
    if user.role == role:
        new_entity = {
            f"{role.lower()}_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "phone_number": user.phone_number,
        }
        repository.create(new_entity)
