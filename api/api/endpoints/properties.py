from flask import abort, make_response

from models import Property, Address, Building, Class, Lot
from schema import properties_schema
from config import db

def read(limit, search_key=None, search_value=None):
    apply_limit = lambda query: query.limit(limit).all()
    if search_key and search_value:
        if search_key == "address":
            properties = apply_limit(db.session.query(Property).join(Address).filter(Address.full_address.contains(search_value)))
        elif search_key == "class":
            properties = apply_limit(db.session.query(Property).join(Building).join(Class).filter(Class.description.contains(search_value)))
        elif search_key == "usage":
            properties = apply_limit(db.session.query(Property).join(Building).filter(Building.usage.contains(search_value)))
        elif search_key == "area":
            properties = apply_limit(db.session.query(Property).join(Building).join(Lot).filter(Lot.building_area.like(f"%{search_value}%")))
        elif search_key == "market_value":
            properties = apply_limit(db.session.query(Property).filter(Property.estimated_market_value.like(f"%{search_value}%")))
        else:
            abort(404, f"Property {search_key} not found")
    else:
        properties = Property.query.limit(limit).all()

    return properties_schema.dump(properties)