
from config import INPUT_PATH

from config import FILE_COLUMNS
from config import ALLOWED_ORDER_STATUS

from config import INVALIDS_PATH
from config import VALIDS_PATH
from config import DUPLICATES_PATH
from config import SUMMARY_PATH

from config import INVALIDS_COLUMNS
from config import VALIDS_COLUMNS
from config import DUPLICATES_COLUMNS
from config import SUMMARY_COLUMNS

from tabulate import tabulate
from reader import read_file
from converter import convert_data
from sifter import split_invalids_valids
from sifter import duplicates_data
from transformer import transform_data
from transformer import summarize_supplier_category
from writer import write_output
from reporter import print_pipeline_output

def execute_sales_pipeline(file_path,output_delimiter):
    raw = read_file(file_path)
    converted = convert_data(raw)

    if not converted:
        return {
            "status": "failed",
            "reason": "conversion failed"
        } 

    invalids, valids = split_invalids_valids(converted)
    duplicates = duplicates_data(invalids)
    transformed = transform_data(valids)
    summary = summarize_supplier_category(transformed)

    write_output(INVALIDS_PATH,invalids,output_delimiter,INVALIDS_COLUMNS)
    write_output(VALIDS_PATH,valids,output_delimiter,VALIDS_COLUMNS)
    write_output(DUPLICATES_PATH,duplicates,output_delimiter,DUPLICATES_COLUMNS)
    write_output(SUMMARY_PATH,transformed,output_delimiter,SUMMARY_COLUMNS)
    print_pipeline_output(raw,invalids,valids,duplicates,summary)

    return {
        "status": "pipeline executed",
        "transformed data": summary
    }


if __name__== "__main__":

    execute_sales_pipeline(INPUT_PATH,"|")

