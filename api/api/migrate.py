import pandas as pd
from config import app, db
from models import Property, Location, Address, Lot, Building, Sale, Class, User

SEED_DATA_ADDRESS = "/Users/mukkundsunjii/projects/proper-ty/seed/Enodo_Skills_Assessment_Data_File.xlsx"

properties_df = pd.read_excel(SEED_DATA_ADDRESS)

properties_df["SALE_DATE"] = properties_df["SALE_DATE"].apply(lambda x: pd.to_datetime(x, errors='coerce'))
properties_df["SALE_DATE"] = properties_df["SALE_DATE"].dt.date
properties_df["SALE_DATE"] = properties_df["SALE_DATE"].astype(object).where(properties_df["SALE_DATE"].notnull(), None)

users = [
    {
        "first_name": "Admin",
        "last_name": "User",
        "username": "admin",
        "password": "admin",
    },
    {
        "first_name": "Basic",
        "last_name": "User",
        "username": "basic",
        "password": "basic",
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()
    building_class_dict = {}

    for index, row in properties_df.iterrows():
        property_record = Property(estimated_market_value=row["ESTIMATED_MARKET_VALUE"], full_bath_count=row["FULL_BATH"], half_bath_count=row["HALF_BATH"], fireplace=row["FIREPLACE"], garage_description=row["GAR_DESC"])
        address = Address(tax_code=row["TAX_CODE"], city=row["CITY"], zip_code=row["Zip"], street=row["STREET"], house_number=row["HOUSENO"], neighborhood=row["NEIGHBORHOOD"], full_address=row["Full Address"])
        location = Location(latitude=row["Latitude"], longitude=row["Longitude"], address=address)
        property_record.location = location
        property_record.address = address
        
        lot = Lot(land_area=row["LAND_SQ_FT"], building_area=row["BUILDING_SQ_FT"])
        unit_count = row["UNITS_TOT"] if type(row["UNITS_TOT"]) is int else None
        commercial_unit_count = row["COMM_UNITS"] if type(row["COMM_UNITS"]) is int else None
        building = Building(building_type="RES_TYPE", usage=row["BLDG_USE"], apartment_count=row["APT"], commercial_unit_count=commercial_unit_count, external_description=row["EXT_DESC"], basement_description=row["BSMT_DESC"], attic_description=row["ATTIC_DESC"], ac_count=row["AC"], age=row["AGE"], unit_count=unit_count, multi_sale=bool(row["MULTI_SALE"]), lot=lot)
        
        building_class = building_class_dict.get(row["OVACLS"])
        if building_class is None:
            building_class_dict[row["OVACLS"]] = Class(class_number=row["OVACLS"], description=row["CLASS_DESCRIPTION"])
        building_class_dict[row["OVACLS"]].buildings.append(building)
        
        property_record.building = building
        sale = Sale(sale_date=row["SALE_DATE"], sale_price=row["SALE_AMOUNT"], asset_property=property_record)
        db.session.add(property_record)
    
    for building_class in building_class_dict.values():
        db.session.add(building_class)

    for user in users:
        db.session.add(User(first_name=user["first_name"], last_name=user["last_name"], username=user["username"], password=user["password"]))
    db.session.commit()