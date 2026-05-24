#standardize string values as uppercase

def clean_data(raw):

    cleaned = []

    for unit in raw:
        homogenized = unit.copy()

        homogenized["vessel_name"] = homogenized["vessel_name"].strip().title()
        homogenized["terminal"] = homogenized["terminal"].strip().title()
        homogenized["cargo_type"] = homogenized["cargo_type"].strip().title()

        cleaned.append (homogenized)

    return cleaned

