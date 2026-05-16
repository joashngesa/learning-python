#output
#item_id
#warehouse_id
#warehouse_region
#product_name
#category
#inventory_value
#reorder_flag

def inventory_value(unit):
    return unit.get("unit_cost") * unit.get("stock_qty")

#reorder_flag = stock_qty <= reorder_level
def reorder_flag(unit):
    if unit.get("stock_qty") <= unit.get("reorder_level"):
        return True
    else:
        return False
    
def transform_data(valids):
    return [
        {
            "item_id": unit.get("item_id"),
            "warehouse_id": unit.get("warehouse_id"),
            "warehouse_region": unit.get("warehouse_region"),
            "product_name": unit.get("product_name"),
            "category": unit.get("category"),
            "inventory_value": inventory_value(unit),
            "reorder_flag": reorder_flag(unit)
        }
        for unit in valids
    ]
