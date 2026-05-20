
#Add derived fields;
    #shipment value(unit_cost * quantity)
    #delivery performance
        #0 to 3 days    → fast
        #4 to 7 days    → normal
        #8+ days        → slow

from validity_splitter import get_invalids_valids

def get_shipment_value(stock):
    return stock.get("unit_cost") * stock.get("quantity")

def get_delivery_performance(stock):
    delivery_days = stock.get("delivery_days")

    if delivery_days <= 3:
        return "fast"
    elif 4 <= delivery_days <= 7:
        return "normal"
    else:
        return "slow"


def get_valids(raw_valids):
    return [
        {
            "shipment_id": stock.get("shipment_id"),
            "supplier_id": stock.get("supplier_id"),
            "supplier_name": stock.get("supplier_name"),
            "region": stock.get("region"),
            "product": stock.get("product"),
            "category": stock.get("category"),
            "unit_cost": stock.get("unit_cost"),
            "quantity": stock.get("quantity"),
            "delivery_days": stock.get("delivery_days"),
            "status": stock.get("status"),
            "shipment_value": get_shipment_value(stock),
            "delivery_performance": get_delivery_performance(stock)
        } for stock in raw_valids
    ]
