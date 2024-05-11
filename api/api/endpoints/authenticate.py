from flask import abort
from models import User

def basic_auth(username, password):
    user = User.query.filter(User.username == username).one_or_none()
    if user is not None and user.password == password:
        return {'sub': username}

    return abort(401, 'Unauthorized')

def authenticate(user):
    return f"User {user} is authenticated."