from config import FILE_COLUMNS
from config import ALLOWED_ORDER_STATUS

def validate_data(po):

    for field in FILE_COLUMNS:
        if field not in po:
            return False, f"the column {field} is missing"
        
    order_id = po.get("order_id")
    supplier_id = po.get("supplier_id")
    supplier_name = po.get("supplier_name")
    category = po.get("category")
    region = po.get("region")
    unit_cost = po.get("unit_cost")
    quantity = po.get("quantity")
    order_status = po.get("order_status")

        #order_id must be non-empty string
        #supplier_id must be non-empty string
        #supplier_name must be non-empty string
        #category must be non-empty string
        #region must be non-empty string
        #unit_cost must be int or float
        #quantity must be int
        #unit_cost must be greater than 0
        #quantity must be greater than 0
        #order_status must be one of: delivered, pending, cancelled, returned

    if not isinstance (order_id,str) or order_id == "":
        return False, "order_id must be non_empty string"
    if not isinstance (supplier_id,str) or supplier_id == "":
        return False, "supplier_id must be non_empty string"
    if not isinstance (supplier_name,str) or supplier_name == "":
        return False, "supplier_name must be non_empty string"
    if not isinstance (category,str) or category == "":
        return False, "category must be non_empty string"
    if not isinstance (region,str) or region == "":
        return False, "region must be non_empty string"
    if not isinstance (unit_cost,(int,float)):
        return False, "unit_cost must be int"
    #i did not use float because i converted the unit cost to int in the previous function(converter)
    if not isinstance (quantity,int):
        return False, "quantity must be int"
    if unit_cost <= 0:
        return False, "unit_cost must be greater than 0"
    if quantity <= 0:
        return False, "quantity must be greater than zero"
    if order_status not in ALLOWED_ORDER_STATUS:
        return False, "order_status must be one of: delivered, pending, cancelled, returned"
    

    return True, None
