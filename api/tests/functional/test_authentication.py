def test_invalid_user(client):
    response = client.get('/api/authenticate')
    assert response.status_code == 401


def test_valid_user(client, basic_auth_header):
    response = client.get('/api/authenticate', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.text == "User admin is authenticated."