#validation rules
# item_id is empty
#warehouse_id is empty
#warehouse_region is empty
#product_name is empty
#category is empty
#unit_cost is not a number
#stock_qty is not an integer
#reorder_level is not an integer
#unit_cost <= 0
#stock_qty <= 0
#reorder_level < 0
#stock_status not allowed...(was i supposed to remove stock_status  from the table?
#i am confused because this is a conversion function not a transformative .)

from config import RAW_COLUMNS

def data_validation(unit):
    
    for field in RAW_COLUMNS:
        if field not in unit:
            return False, f"the column {field} is missing"
        
    item_id = unit.get("item_id")
    warehouse_id = unit.get("warehouse_id")
    warehouse_region = unit.get("warehouse_region")
    product_name = unit.get("product_name")
    category = unit.get("category")
    unit_cost = unit.get("unit_cost")
    stock_qty = unit.get("stock_qty")
    reorder_level = unit.get("reorder_level")
    stock_status = unit.get("stock_status")

    if not isinstance (item_id,str) or item_id == "":
        return False, "item_id should be a non_empty string"
    if not isinstance (warehouse_id,str) or warehouse_id == "":
        return False, "warehouse_id should be a non_empty string"
    if not isinstance (warehouse_region,str) or warehouse_region == "":
        return False, "warehouse region should be a non_empty string"
    if not isinstance (product_name,str) or product_name == "":
        return False, "product_name should be non empty string"
    if not isinstance (category,str) or category == "":
        return False, "category shoud be non empty string"
    if not isinstance (unit_cost,(float,int)):
        return False, "unit_cost should be a number"
    if unit_cost <= 0:
        return False, "unit_cost should be greater than zero"
    if not isinstance (stock_qty,int):
        return False, "stock quantity should be integer"
    if stock_qty <= 0:
        return False, "stock_qty should be greater than zero"
    if not isinstance (reorder_level,int):
        return False, "reorder_level should be integer"
    if reorder_level < 0:
        return False, "reorder_level shoild not be less than zero"
    if not isinstance (stock_status,str) or stock_status == "":
        return False, "stock_status should be non empty string"
    
    return True, None