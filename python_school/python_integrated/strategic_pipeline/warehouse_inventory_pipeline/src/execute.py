
from config import INPUT_PATH

from config import VALIDS_PATH
from config import VALIDS_COLUMN

from config import INVALIDS_PATH
from config import INVALIDS_COLUMN

from config import DUPLICATES_PATH
from config import DUPLICATES_COLUMN

from config import TRANSFORMED_PATH
from config import TRANSFORMED_COLUMN

from config import SUMMARY_PATH
from config import SUMMARY_COLUMN

from reader import read_data
from converter import convert_data
from invalids_valid_sifter import sifter
from invalids_valid_sifter import duplicate_data
from transformer import transform_data 
from summary import summarize_data
from writer import write_csv
from reporter import print_pipeline_output

def execute_warehouse_pipeline(file_path,output_delimiter):
    raw = read_data(file_path)
    converted = convert_data(raw)

    if not converted:
        return {
            "status": "failed",
            "reason": "conversion failed"
        }

    invalids, valids = sifter(converted)
    duplicates = duplicate_data(invalids)
    transformed = transform_data(valids)
    summary = summarize_data(transformed)

    write_csv(INVALIDS_PATH,invalids,output_delimiter,INVALIDS_COLUMN)
    write_csv(VALIDS_PATH,valids,output_delimiter,VALIDS_COLUMN)
    write_csv(DUPLICATES_PATH,duplicates,output_delimiter,DUPLICATES_COLUMN)
    write_csv(TRANSFORMED_PATH,transformed,output_delimiter,TRANSFORMED_COLUMN)
    write_csv(SUMMARY_PATH,summary,output_delimiter,SUMMARY_COLUMN)

    print_pipeline_output(raw,invalids,valids,duplicates,transformed,summary)

if __name__=="__main__":

    execute_warehouse_pipeline(INPUT_PATH,"|")