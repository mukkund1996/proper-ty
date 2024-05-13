from flask import abort, make_response

from api import db
from api.models import User, UserPropertyRelation
from api.schema import user_schema, users_schema, user_relation_schema, user_relations_schema

def read_all():
    """Retrieves a list of all users."""
    users = User.query.all()
    return users_schema.dump(users)

def create(user):
    """
    Create a new user.

    Args:
        user (dict): A dictionary containing the user information.

    Returns:
        tuple: A tuple containing the serialized user object and the HTTP status code.

    Raises:
        HTTPException: If the user already exists.
    """
    username = user.get("username")
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"User {username} exists already")
    

def read_one(user_id):
    """
    Retrieve a single user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's information.

    Raises:
        NotFound: If the user with the specified ID is not found.
    """
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        return user_schema.dump(user)
    else:
        abort(404, f"User {user_id} not found")

def update(user_id, user):
    """
    Update a user with the given user_id.

    Args:
        user_id (int): The ID of the user to update.
        user (dict): The updated user data.

    Returns:
        tuple: A tuple containing the updated user data and the HTTP status code.

    Raises:
        NotFound: If the user with the given user_id is not found.
    """
    existing_user = User.query.filter(User.id == user_id).one_or_none()
    if existing_user is not None:
        updated_user = user_schema.load(user, session=db.session)
        existing_user.first_name = updated_user.first_name
        existing_user.last_name = updated_user.last_name
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 200
    else:
        abort(404, f"User {user_id} not found")

def delete(user_id):
    """
    Delete a user by their ID.

    Args:
        user_id (int): The ID of the user to be deleted.

    Returns:
        Response: A response indicating the success or failure of the deletion.

    Raises:
        NotFound: If the user with the specified ID is not found.
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {user_id} deleted", 204)
    else:
        abort(404, f"User {user_id} not found")


def add_property(user_property_relation):
    """
    Add a property to a user.

    Args:
        user_property_relation (dict): A dictionary containing the user_id and property_id.

    Returns:
        tuple: A tuple containing the serialized user-property relation and the HTTP status code.

    Raises:
        NotFound: If the user with the given user_id is not found.
    """
    user_id = user_property_relation.get("user_id")
    property_id = user_property_relation.get("property_id")
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        relation = UserPropertyRelation(user_id=user_id, property_id=property_id)
        db.session.add(relation)
        db.session.commit()
        return user_relation_schema.dump(relation), 200
    else:
        abort(404, f"User {user_id} not found")

def get_properties(user_id):
    """
    Retrieve the properties associated with a user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        tuple: A tuple containing the serialized user-property relations and the HTTP status code.

    Raises:
        HTTPException: If the user with the given ID is not found.
    """
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        relations = UserPropertyRelation.query.filter(UserPropertyRelation.user_id == user_id).all()
        return user_relations_schema.dump(relations), 200
    else:
        abort(404, f"User {user_id} not found")