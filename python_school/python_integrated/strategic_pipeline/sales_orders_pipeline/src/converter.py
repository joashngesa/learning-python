def convert_data(raw):

    converted = []
    for po in raw:
        conv = po.copy()

        try:
            conv["unit_cost"] = float(conv["unit_cost"]) if conv["unit_cost"] != "" else None

        except ValueError:
            conv["unit_cost"] = None

        try:
            conv["quantity"] = int(conv["quantity"]) if conv["quantity"] != ""else None

        except ValueError:
            conv["quantity"] = None

        converted.append(conv)

    return converted