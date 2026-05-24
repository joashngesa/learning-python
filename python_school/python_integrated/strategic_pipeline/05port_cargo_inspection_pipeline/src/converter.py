#Rules:
    #empty string becomes None
    #failed conversion becomes None
    #do not validate here
    #preserve existing error_reasons

def convert_data (cleaned):

    converted = []

    for unit in cleaned:
        translated = unit.copy()

        try:
            translated["weight_kg"] = int (translated["weight_kg"]) if translated["weight_kg"] != "" else None 
        except ValueError:
            translated["weight_kg"] = None

        try:
            translated["risk_score"] = int (translated["risk_score"]) if translated["risk_score"] != "" else None
        except ValueError:
            translated["risk_score"] = None

        try:
            translated["inspection_minutes"] = int (translated["inspection_minutes"]) if translated["inspection_minutes"] != "" else None
        except ValueError:
            translated["inspection_minutes"] = None

        converted.append (translated)

    return converted
            