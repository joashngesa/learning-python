
#Duplicate check using multi key;
    #(shipment_id, supplier_id)

from validator import validate_data

def get_invalids_valids(converted):

    invalids = []
    raw_valids = []
    seen_ids = set()

    for stock in converted:
        is_valid, reasons = validate_data(stock)

        if not is_valid:
            inaccurate = stock.copy()
            inaccurate["error_reasons"] = reasons
            invalids.append (inaccurate)
            continue

        shipment_id = stock.get("shipment_id")
        supplier_id = stock.get("supplier_id")
        checks = (shipment_id,supplier_id)

        if checks in seen_ids:
            inaccurate = stock.copy()
            inaccurate["error_reasons"] = "duplicate shipment_id & supplier_id"
            invalids.append (inaccurate)
            continue

        seen_ids.add (checks)
        raw_valids.append (stock.copy())

    return invalids, raw_valids



#when it comes to identifying the errors, the rows with extra fields, i dont know
#how to bring theem out in the invalids table, in revision of the answer, break down 
#the codes that can be used to do this, explain them extensively. from the code i used
