from api.models import Location, Address

def test_location():
    """
    GIVEN a Location model
    WHEN a new Location is created
    THEN check the address_id, location_name, and location_type fields are defined correctly
    """
    location = Location(address_id=1, latitude=1.0, longitude=1.4)
    assert location.address_id == 1
    assert location.latitude == 1.0
    assert location.longitude == 1.4

def test_address():
    """
    GIVEN a Address model
    WHEN a new Address is created
    THEN check the street_number, street_name, city, state, and zip_code fields are defined correctly
    """
    address = Address(street="Test", city="Test", town=5, zip_code=12345, tax_code=1236, house_number=1, neighborhood=5, full_address="Test")
    assert address.street == "Test"
    assert address.city == "Test"
    assert address.zip_code == 12345
    assert address.town == 5
    assert address.tax_code == 1236
    assert address.neighborhood == 5
    assert address.full_address == "Test"

