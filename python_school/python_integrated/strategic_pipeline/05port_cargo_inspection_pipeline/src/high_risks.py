
#high risks rule;
    #risk_score >= 80
def get_high_risks(valids):
    return [unit for unit in valids if unit.get("risk_score") >= 80 ]