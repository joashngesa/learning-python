#cleaning rules
    #supplier_name → title case and trim spaces
    #region        → title case and trim spaces
    #product       → title case and trim spaces
    #category      → title case and trim spaces
    #status        → lowercase and trim spaces

def clean_data(raw_data):

    cleaned = []

    for stock in raw_data:
        standard = stock.copy()

        standard["supplier_name"] = standard.get("supplier_name").strip().title()
        standard["region"] = standard.get("region").strip().title()
        standard["product"] = standard.get("product").strip().title()
        standard["category"] = standard.get("category").strip().title()
        standard["status"] = standard.get("status").strip().lower()

        cleaned.append (standard)

    return cleaned