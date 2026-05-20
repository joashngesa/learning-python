#group by region
    #region
    #shipment_count
    #total_quantity
    #total_value
    #avg_delivery_days 
    #slow_shipments

def region_summ(valids):

    region_sum = {}

    for stock in valids:

        region = stock.get("region")
        quantity = stock.get("quantity")
        shipment_value = stock.get("shipment_value")
        delivery_days = stock.get("delivery_days")
        delivery_performance = stock.get("delivery_performance")

        if region not in region_sum:
            region_sum[region] = {
                "region": region,
                "shipment_count": 0,
                "total_quantity": 0,
                "total_value": 0,
                "slow_shipment": 0,
                "avg_delivery_days": 0,
                "tot_delivery_days": 0
            }

        region_sum[region]["shipment_count"] += 1 
        region_sum[region]["total_quantity"] += quantity
        region_sum[region]["total_value"] += shipment_value
        region_sum[region]["tot_delivery_days"] += delivery_days 

        if delivery_performance  == "slow":
            region_sum[region]["slow_shipment"] += 1

    for area in region_sum:
        data = region_sum[area]
        data["avg_delivery_days"] = round(data["tot_delivery_days"] / data["shipment_count"],2)
        del data["tot_delivery_days"]

    return list (region_sum.values())



