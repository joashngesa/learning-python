
#group by:
    #supplier_id
    #supplier_name

#expected columns
    #supplier_id
    #supplier_name
    #shipment_count
    #total_quantity
    #total_value
    #avg_delivery_days

def supplier_summ(valids):

    supplier_sm = {}

    for stock in valids:

        supplier_id = stock.get("supplier_id")
        supplier_name = stock.get("supplier_name")
        shipment_value = stock.get("shipment_value")
        quantity = stock.get("quantity")
        delivery_days = stock.get("delivery_days")
        keys = (supplier_id,supplier_name)

        if keys not in supplier_sm:
            supplier_sm[keys] = {
                "supplier_id": supplier_id,
                "supplier_name": supplier_name,
                "shipment_count": 0,
                "total_quantity": 0,
                "total_value": 0,
                "avg_delivery_days": 0,
                "total_delivery_days": 0
            }

        supplier_sm[keys]["shipment_count"] += 1
        supplier_sm[keys]["total_quantity"] += quantity
        supplier_sm[keys]["total_value"] += shipment_value
        supplier_sm[keys]["total_delivery_days"] += delivery_days

        new = []
        for supp in supplier_sm:
            supp = supplier_sm[supp]
            supp["avg_delivery_days"] = (supp["total_delivery_days"] / supp["shipment_count"])


            
        #this only works because the shipment count is 1. Explain how to calc average the proper way
        #supplier_sm[keys]["avg_delivery_days"] = (delivery_days / 
                                                     #supplier_sm[keys]["shipment_count"])

         
    return list (supplier_sm.values())