#output fields
    #warehouse_region
    #category
    #total_inventory_value
    #item_count
    #reorder_item_count

    #total_inventory_value = sum of inventory_value
    #item_count = number of transformed records in that group
    #reorder_item_count = number of records where reorder_flag is True

def summarize_data(transformed):

    summary = {}

    for unit in transformed:
        warehouse_region = unit.get("warehouse_region")
        category = unit.get("category")
        inventory_value = unit.get("inventory_value")
        reorder_flag = unit.get("reorder_flag")
        keys = (warehouse_region, category)

        if keys not in summary:
            summary[keys] = {
                "warehouse_region": warehouse_region,
                "category": category,
                "total_inventory_value": 0,
                "item_count": 0,
                "reorder_item_count": 0
            }

        summary[keys]["total_inventory_value"] += inventory_value
        summary[keys]["item_count"] += 1 
        if reorder_flag:
             summary[keys]["reorder_item_count"] += 1

    return list(summary.values())