from src.config import INPUT_PATH

def read_data(file_path):

    raw = []

    try:

        with open (file_path, "r", newline="", encoding="utf-8-sig") as file:
            next(file)

            for cargo in file:
                parsed = cargo.strip().split("|")

                if len(parsed) != 10:
                    raw.append({
                            "inspection_id": "",
                            "container_id": "",
                            "vessel_name": "",
                            "terminal": "",
                            "cargo_type": "",
                            "origin_country": "",
                            "weight_kg": "",
                            "risk_score": "",
                            "inspection_minutes": "",
                            "status": "",
                            "error_reasons": "row does not have exactly 10 fields",
                            "extra_lines": cargo.strip()
                        })
                    continue

                inspection_id = parsed[0].strip()
                container_id = parsed[1].strip()
                vessel_name = parsed[2].strip()
                terminal = parsed[3].strip()
                cargo_type = parsed[4].strip()
                origin_country = parsed[5].strip()
                weight_kg = parsed[6].strip()
                risk_score = parsed[7].strip()
                inspection_minutes = parsed[8].strip()
                status = parsed[9].strip()

                new = {
                        "inspection_id": inspection_id,
                        "container_id": container_id,
                        "vessel_name": vessel_name,
                        "terminal": terminal,
                        "cargo_type": cargo_type,
                        "origin_country": origin_country,
                        "weight_kg": weight_kg,
                        "risk_score": risk_score,
                        "inspection_minutes": inspection_minutes,
                        "status": status,
                        "error_reasons": "",
                        "extra_lines": ""
                    }

                raw.append(new)

    except Exception as e:
        print(f"File reading error: {e}")
        return []

    return raw