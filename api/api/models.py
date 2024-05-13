from api import db

class Sale(db.Model):
    __tablename__ = 'sale'
    id = db.Column(db.Integer, primary_key=True)
    asset_property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    sale_price = db.Column(db.Float)
    sale_date = db.Column(db.Date)
    asset_property = db.relationship('Property', back_populates='sale')

class Lot(db.Model):
    __tablename__ = 'lot'
    id = db.Column(db.Integer, primary_key=True)
    land_area = db.Column(db.Float)
    building_area = db.Column(db.Float)
    
    building = db.relationship('Building', back_populates='lot')

class Building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    lot_id = db.Column(db.Integer, db.ForeignKey('lot.id'))
    building_type = db.Column(db.String[70])
    usage = db.Column(db.String[70])
    apartment_count = db.Column(db.String[30])
    commercial_unit_count = db.Column(db.Integer)
    external_description = db.Column(db.String[70])
    basement_description = db.Column(db.String[70])
    attic_description = db.Column(db.String[70])
    ac_count = db.Column(db.Integer)
    age = db.Column(db.Integer)
    unit_count = db.Column(db.Integer)
    multi_sale = db.Column(db.Boolean)
    
    building_class = db.relationship('Class', back_populates='buildings')
    lot = db.relationship(Lot, back_populates='building')
    asset_properties = db.relationship('Property', back_populates='building')

class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    class_number = db.Column(db.Integer, unique=True)
    description = db.Column(db.String[70])

    buildings = db.relationship(Building, back_populates='building_class', single_parent=True)

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    address = db.relationship('Address', back_populates='locations')
    asset_property = db.relationship('Property', back_populates='location')

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    tax_code = db.Column(db.Integer)
    town = db.Column(db.Integer)
    city = db.Column(db.String[70])
    street = db.Column(db.String[70])
    house_number = db.Column(db.Integer)
    neighborhood = db.Column(db.Integer)
    full_address = db.Column(db.String[70])
    zip_code = db.Column(db.Integer)

    asset_property = db.relationship('Property', back_populates='address')
    locations = db.relationship(Location, back_populates='address')

class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    
    estimated_market_value = db.Column(db.Float)
    full_bath_count = db.Column(db.Integer)
    half_bath_count = db.Column(db.Integer)
    fireplace = db.Column(db.Integer)
    garage_description = db.Column(db.String[70])

    sale = db.relationship(Sale, back_populates='asset_property', single_parent=True, cascade='all, delete, delete-orphan')
    building = db.relationship(Building, back_populates='asset_properties')
    location = db.relationship(Location, back_populates='asset_property')
    address = db.relationship(Address, back_populates='asset_property')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

class UserPropertyRelation(db.Model):
    __tablename__ = 'user_property_relation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
