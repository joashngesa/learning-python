#convert the below column values to string:
    #unit_cost
    #quantity
    #delivery_days

def convert_data(cleaned):

    converted = []

    for stock in cleaned:
        new = stock.copy()

        try:
            new["unit_cost"] = float (new["unit_cost"]) if new["unit_cost"] != "" else None
        except ValueError:
            new["unit_cost"] = None

        try:
            new["quantity"] = int (new["quantity"]) if new["quantity"] != "" else None
        except ValueError:
            new["quantity"] = None

        try:
            new["delivery_days"] = int (new["delivery_days"]) if new["delivery_days"] != "" else None
        except ValueError:
            new["delivery_days"] = None

        converted.append(new)

    return converted