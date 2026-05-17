#convert the following columns:
#unit_cost → float
#stock_qty → int
#reorder_level → int

def convert_data(raw):

    converted = []

    for unit in raw:
        conv = unit.copy()
        
        try:
            conv["unit_cost"] = float(conv["unit_cost"]) if conv["unit_cost"] != "" else None
        except ValueError:
            conv["unit_cost"] = None

        try:
            conv["stock_qty"] = int (conv["stock_qty"]) if conv["stock_qty"] != "" else None
        except ValueError:
            conv["stock_qty"] = None

        try:
            conv["reorder_level"] = int (conv["reorder_level"]) if conv["reorder_level"] != "" else None
        except ValueError:
            conv["reorder_level"] = None

        converted.append(conv)

    return converted