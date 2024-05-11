from api.models import Sale

def test_sale():
    """
    GIVEN a Sale model
    WHEN a new Sale is created
    THEN check the sale_date, sale_price, sale_id, and property_id fields are defined correctly
    """
    sale = Sale(sale_date="2021-01-01", sale_price=100000, asset_property_id=1)
    assert sale.sale_date == "2021-01-01"
    assert sale.sale_price == 100000
    assert sale.asset_property_id == 1