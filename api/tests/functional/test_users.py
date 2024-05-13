from api.models import User
from api.schema import user_schema


def test_get_users(client, basic_auth_header):
    response = client.get('/api/users', headers=basic_auth_header)
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['username'] == 'admin'

def test_get_single_user(client, basic_auth_header):
    response = client.get('/api/users/1', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.json['username'] == 'admin'
    assert response.json["first_name"] == "Admin"
