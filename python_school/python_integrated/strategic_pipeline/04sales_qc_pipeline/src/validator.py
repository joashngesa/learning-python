#VALIDATION RULES
#These fields should not be blank  
    #shipment_id
    #supplier_id
    #supplier_name
    #region
    #product
    #category
    #unit_cost
        #non-empty
        #numeric
        #greater than 0
    #quantity
        #non-empty
        #integer
        #greater than 0
    #delivery_days
        #non-empty
        #integer
        #greater than or equal to 0
    #status
        #allowed status; {"delivered", "delayed", "cancelled", "in_transit"}

from config import FILE_COLUMNS

allowed_status =["delivered", "delayed", "cancelled", "in_transit"]

def validate_data(stock):

    errors = stock.get("error_reasons")
    if errors:
        return False, "parse error"
    
    for column in FILE_COLUMNS:
        if column not in stock:
            return False, f"the column {column} is missing "

    shipment_id = stock.get("shipment_id")
    supplier_id = stock.get("supplier_id")
    supplier_name = stock.get("supplier_name")
    region = stock.get("region")
    product = stock.get("product")
    category = stock.get("category")
    unit_cost = stock.get("unit_cost")
    quantity = stock.get("quantity")
    delivery_days = stock.get("delivery_days")
    status = stock.get("status")

    if shipment_id is None:
        return False, "shipment_id is missing from the data"
    if not isinstance (shipment_id, str) :
        return False, "shipment_id is not a string"
    if not shipment_id.strip():
        return False, "shipment_id is blank"
    if supplier_id is None:
        return False, "the supplier_id is missing from the data"
    if not isinstance (supplier_id,str):
        return False, "supplier_id is not a string"
    if not supplier_id.strip():
        return False, "supplier_id is blank"
    if supplier_name is None:
        return False, "the supplier_name is missing from the data"
    if not isinstance (supplier_name,str):
        return False, "supplier name is not a string"
    if not supplier_name.strip():
        return False, "the supplier_name is blank"
    if region is None:
        return False, "region is missing from the data"
    if not isinstance (region,str):
        return False, "region is not a string"
    if not region.strip():
        return False, "region is blank"
    if product is None:
        return False, "product is missing from the data"
    if not isinstance (product,str):
        return False, "product is not a string"
    if not product.strip():
        return False, "product is blank" 
    if category is None:
        return False, "category isn missing from the data"
    if not isinstance (category,str):
        return False, "category is not a string"
    if not category.strip():
        return False, "category is blank"
    if not isinstance (unit_cost,(float,int)):
        return False, "unit_cost should be a valid number"
    if unit_cost <= 0:
        return False, "unit_cost should be greater than zero "
    if not isinstance (quantity,int):
        return False, "quantity should be integer"
    if quantity <= 0:
        return False, "quantity should be greater than zero"
    if not isinstance (delivery_days,int):
        return False, "delivery_days should be integer"
    if delivery_days < 0:
        return False, "delivery_days should be equal to or greater than 0"
    if status not in allowed_status:
        return False, f"invalid status: {status}. must be one of {allowed_status}"
    
    return True, None


    
