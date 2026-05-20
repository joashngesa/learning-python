
from config import INPUT_PATH

from config import VALIDS_PATH
from config import INVALIDS_PATH
from config import SUPPLIER_SUMMARY_PATH
from config import REGION_SUMMARY_PATH

from reader import read_file
from cleaner import clean_data
from converter import convert_data
from validity_splitter import get_invalids_valids
from valids import get_valids
from supplier_summary import supplier_summ
from region_summary import region_summ
from writer import write_output
from feedback import output_report

valids_column = ["shipment_id","supplier_id","supplier_name","region",
                "product","category","unit_cost","quantity",
                "delivery_days","status","shipment_value","delivery_performance"]
invalids_column = ["shipment_id","supplier_id","supplier_name","region",
                "product","category","unit_cost","quantity",
                "delivery_days","status","error_reasons"]
suppliers_column = ["supplier_id","supplier_name","shipment_count","total_quantity","total_value","avg_delivery_days"]
region_column = ["region","shipment_count","total_quantity","total_value","slow_shipment","avg_delivery_days","tot_delivery_days"]

def execute_shipment_qc (file_path,output_delimiter):

    raw = read_file(file_path)
    cleaned = clean_data (raw)
    converted = convert_data (cleaned)
    invalids, raw_valids = get_invalids_valids(converted)
    valids = get_valids(raw_valids)
    supplier_synopsis = supplier_summ(valids)
    region_synopsis = region_summ(valids)

    write_output (VALIDS_PATH,valids,output_delimiter,valids_column)
    write_output (INVALIDS_PATH,invalids,output_delimiter,invalids_column)
    write_output (SUPPLIER_SUMMARY_PATH,supplier_synopsis,output_delimiter,suppliers_column)
    write_output (REGION_SUMMARY_PATH,region_synopsis,output_delimiter,region_column)

    output_report (raw,valids,invalids)


if __name__=="__main__":

    execute_shipment_qc(INPUT_PATH,"|")