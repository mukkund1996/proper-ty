def test_get_limited_properties(client, basic_auth_header):
    response = client.get('/api/properties?limit=2', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.json["countPerPage"] == 2
    assert response.json["properties"][0]['address']["full_address"] == '210 N JUSTINE ST, CHICAGO, IL'
    assert response.json["properties"][1]['address']["full_address"] == '1529 W TAYLOR ST, CHICAGO, IL'

def test_get_paginated_properties(client, basic_auth_header):
    response = client.get('/api/properties?page=10&page_size=2', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.json["countPerPage"] == 2
    assert response.json["properties"][0]["id"] == 19
    assert response.json["properties"][1]["id"] == 20

def test_get_filtered_properties(client, basic_auth_header):
    response = client.get('/api/properties?search_key=address&search_value=1529%20W%20TAYLOR%20ST', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.json["countPerPage"] == 1
    assert response.json["properties"][0]["id"] == 2
    assert response.json["properties"][0]['address']["full_address"] == '1529 W TAYLOR ST, CHICAGO, IL'

def test_get_properties_metadata(client, basic_auth_header):
    response = client.get('/api/properties/meta?page_size=10', headers=basic_auth_header)
    assert response.status_code == 200
    assert response.json["totalPages"] == 150
    assert response.json["totalCount"] == 1500

    
