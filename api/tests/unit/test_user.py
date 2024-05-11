from api.models import User

def test_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, first_name, last_name, and password fields are defined correctly
    """
    user = User(username="test", first_name="Test", last_name="User", password="password")
    assert user.username == "test"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.password == "password"