from config import db, ma
from models import User, Property, Address, Location, Building, Lot
from marshmallow_sqlalchemy import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True
        sqla_session = db.session
        include_fk = True

address_schema = AddressSchema()

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        load_instance = True
        sqla_session = db.session
        include_fk = True

location_schema = LocationSchema()

class LotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lot
        load_instance = True
        sqla_session = db.session

lot_schema = LotSchema()

class BuildingClassSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Building
        load_instance = True
        sqla_session = db.session

building_class_schema = BuildingClassSchema()

class BuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Building
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    building_class = fields.Nested(BuildingClassSchema)
    lot = fields.Nested(LotSchema)

building_schema = BuildingSchema()


class SaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Property
        load_instance = True
        sqla_session = db.session
        include_fk = True

sale_schema = SaleSchema()

class PropertySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Property
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    
    building = fields.Nested(BuildingSchema)
    sale = fields.Nested(SaleSchema)
    location = fields.Nested(LocationSchema)
    address = fields.Nested(AddressSchema)

property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)