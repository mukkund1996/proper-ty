from flask import abort, make_response

from config import db
from models import User, UserPropertyRelation
from schema import user_schema, users_schema, user_relation_schema, user_relations_schema

def read_all():
    users = User.query.all()
    return users_schema.dump(users)

def create(user):
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
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        return user_schema.dump(user)
    else:
        abort(404, f"User {user_id} not found")

def update(user_id, user):
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
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {user_id} deleted", 204)
    else:
        abort(404, f"User {user_id} not found")


def add_property(user_property_relation):
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
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        relations = UserPropertyRelation.query.filter(UserPropertyRelation.user_id == user_id).all()
        return user_relations_schema.dump(relations), 200
    else:
        abort(404, f"User {user_id} not found")