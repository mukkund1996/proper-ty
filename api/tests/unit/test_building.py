from api.models import Building, Lot, Class

def test_building():
    """
    GIVEN a Building model
    WHEN a new Building is created
    THEN check the class_id, lot_id, building_type, usage, apartment_count, commercial_unit_count, external_description, basement_description, attic_description, ac_count, age, unit_count, and multi_sale fields are defined correctly
    """
    building = Building(class_id=1, lot_id=1, building_type="test", usage="test", apartment_count="test", commercial_unit_count=1, external_description="test", basement_description="test", attic_description="test", ac_count=1, age=1, unit_count=1, multi_sale=True)
    assert building.class_id == 1
    assert building.lot_id == 1
    assert building.building_type == "test"
    assert building.usage == "test"
    assert building.apartment_count == "test"
    assert building.commercial_unit_count == 1
    assert building.external_description == "test"
    assert building.basement_description == "test"
    assert building.attic_description == "test"
    assert building.ac_count == 1
    assert building.age == 1
    assert building.unit_count == 1
    assert building.multi_sale == True

def test_lot():
    """
    GIVEN a Lot model
    WHEN a new Lot is created
    THEN check the land_area and building_area fields are defined correctly
    """
    lot = Lot(land_area=1.0, building_area=1.0)
    assert lot.land_area == 1.0
    assert lot.building_area == 1.0

def test_building_class():
    """
    GIVEN a Class model
    WHEN a new Class is created
    THEN check the class_number and description fields are defined correctly
    """
    building_class = Class(class_number=1, description="test")
    assert building_class.class_number == 1
    assert building_class.description == "test"