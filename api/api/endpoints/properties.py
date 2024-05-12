from flask import abort, make_response

from models import Property, Address, Building, Class, Lot
from schema import properties_schema
from config import db

def read(limit, page=None, page_size=None, search_key=None, search_value=None):
    base_query = db.session.query(Property)
    if search_key and search_value:
        if search_key == "address":
            properties_query = base_query.join(Address).filter(Address.full_address.contains(search_value))
        elif search_key == "class":
            properties_query = base_query.join(Building).join(Class).filter(Class.description.contains(search_value))
        elif search_key == "usage":
            properties_query = base_query.join(Building).filter(Building.usage.contains(search_value))
        elif search_key == "area":
            properties_query = base_query.join(Building).join(Lot).filter(Lot.building_area.like(f"%{search_value}%"))
        elif search_key == "marketValue":
            properties_query = base_query.filter(Property.estimated_market_value.like(f"%{search_value}%"))
        else:
            abort(404, f"Property {search_key} not found")
    else:
        properties_query = base_query

    if page and page_size:
        page_count = properties_query.count() // page_size
        properties = db.paginate(properties_query, page=page, per_page=page_size)
    else:
        page_count = None
        properties = properties_query.limit(limit)

    properties_response = properties_schema.dump(properties)
    num_properties = len(properties_response)

    return {
        "properties": properties_response,
        "countPerPage": num_properties,
        "totalCount": num_properties * page_count if page_count else num_properties,
        "totalPages": page_count
    }

def get_meta(page_size=None):
    properties_count = db.session.query(Property).count()
    response = {
        "totalCount": properties_count,
    }
    if page_size:
        response["totalPages"] = properties_count // page_size
    
    return make_response(response, 200)