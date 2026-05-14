#should contain;
    #calculate_total_cost(record)
    #transform_supplier_orders(valid_records)
    #summarize_by_supplier_category(transformed_records)

#oiutput fields
    #supplier_name
    #category
    #total_cost
    #order_count

def calc_tot_cost(po):
    return po.get("unit_cost") * po.get("quantity")

def transform_data(valids):

    transformed = []
    for po in valids:
        supplier_name = po.get("supplier_name")
        category = po.get("category")

        transformed.append({
            "supplier_name": supplier_name,
            "category": category,
            "total_cost": calc_tot_cost(po)
        })

    return transformed

def summarize_supplier_category(transformed):

    summary = {}

    for po in transformed:
        supplier_name = po.get("supplier_name")
        category = po.get("category")
        total_cost = po.get("total_cost")
        keys = (supplier_name, category)

        if keys not in summary:
            summary[keys] = {
                "supplier_name": supplier_name,
                "category": category,
                "total_cost": 0,
                "order_count": 0
            }

        summary[keys]["total_cost"] += total_cost
        summary[keys]["order_count"] += 1

    return list(summary.values())