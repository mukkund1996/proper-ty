from flask import abort, make_response

from models import Property, Address, Building, Class, Lot
from schema import properties_schema
from api import db, cache

@cache.memoize(timeout=1000)
def read(limit, page=None, page_size=None, search_key=None, search_value=None):
    """
    Retrieves a list of properties based on the provided parameters.

    Args:
        limit (int): The maximum number of properties to retrieve.
        page (int, optional): The page number to retrieve when paginating results. Defaults to None.
        page_size (int, optional): The number of properties per page when paginating results. Defaults to None.
        search_key (str, optional): The property attribute to search for. Defaults to None.
        search_value (str, optional): The value to search for in the specified property attribute. Defaults to None.

    Returns:
        dict: A dictionary containing the retrieved properties and additional information.
            - properties (list): A list of property objects.
            - countPerPage (int): The number of properties per page.
            - totalCount (int): The total number of properties.
            - totalPages (int): The total number of pages.

    Raises:
        404: If the specified search_key is not found.
    """
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

@cache.memoize(timeout=1000)
def get_meta(page_size=None):
    """
    Get metadata for properties.

    Args:
        page_size (int, optional): The number of properties per page. Defaults to None.

    Returns:
        dict: A dictionary containing the metadata.
            - totalCount (int): The total count of properties.
            - totalPages (int, optional): The total number of pages based on the page size.
    """
    properties_count = db.session.query(Property).count()
    response = {
        "totalCount": properties_count,
    }
    if page_size:
        response["totalPages"] = properties_count // page_size
    
    return make_response(response, 200)