
from src.config import INPUT_PATH

from src.config import VALIDS_PATH
from src.config import INVALIDS_PATH
from src.config import SUMMARY_PATH
from src.config import HIGH_RISK_PATH

from src.reader import read_data
from src.cleaner import clean_data
from src.converter import convert_data
from src.validity_splitter import get_invalids_valids
from src.valids import get_valids
from src.terminal_aggregator import summarize_terminal_cargo
from src.high_risks import get_high_risks
from src.writer import write_output

valids_column = ["inspection_id","container_id","vessel_name",
               "terminal","cargo_type","origin_country",
               "weight_kg","risk_score","inspection_minutes"
               ,"status"]
invalids_column = ["inspection_id","container_id","vessel_name",
               "terminal","cargo_type","origin_country",
               "weight_kg","risk_score","inspection_minutes"
               ,"status","error_reasons"]
summary_column = ["container_count","total_weight_kg","average_risk_score",
                  "average_inspection_minutes","held_count","rejected_count"]
high_risks_column = ["inspection_id","container_id","vessel_name","terminal",
                     "cargo_type","origin_country","weight_kg","risk_score",
                     "inspection_minutes","status"]

def execute_inspection_pipeline (file_path,output_delimiter):

    raw = read_data(file_path)
    cleaned = clean_data(raw)
    converted = convert_data(cleaned)
    invalids, raw_valids = get_invalids_valids(converted)
    valids = get_valids(raw_valids)
    summary = summarize_terminal_cargo(valids)
    high_risks = get_high_risks(valids)

    write_output (INVALIDS_PATH,invalids,output_delimiter,invalids_column)
    write_output (VALIDS_PATH,valids,output_delimiter,valids_column)
    write_output (SUMMARY_PATH,summary,output_delimiter,summary_column)
    write_output (HIGH_RISK_PATH,high_risks,output_delimiter,high_risks_column)

    print("pipeline successful")
    print("\nvalid table count: ",len(valids))
    print("\ninvalids table count: ",len(invalids))

if __name__=="__main__":

    execute_inspection_pipeline(INPUT_PATH,"|")
    