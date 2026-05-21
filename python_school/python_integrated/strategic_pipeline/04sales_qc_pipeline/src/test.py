from tabulate import tabulate

from reader import read_file
from config import INPUT_PATH
from cleaner import clean_data
from converter import convert_data
from validity_splitter import get_invalids_valids
from valids import get_valids
from supplier_summary import supplier_summ
from region_summary import region_summ

raw_data = read_file (INPUT_PATH)
print ("\nraw data")
print ("row_number: ",len(raw_data))
print(tabulate(raw_data, headers="keys", tablefmt="grid"))

cleaned = clean_data (raw_data)
print ("\ncleaned data")
print ("\nrow_number: ",len(cleaned))
print(tabulate(cleaned, headers="keys", tablefmt="grid"))

converted = convert_data(cleaned)
print ("\nconverted data")
print("\nrow_number: ",len(converted))
print(tabulate(converted, headers="keys", tablefmt="grid"))

invalids, raw_valids = get_invalids_valids(converted)
print ("\ninvalid data")
print(tabulate(invalids, headers="keys", tablefmt="grid"))
print ("\nvalid_raw data")
print(tabulate(raw_valids, headers="keys", tablefmt="grid"))

valids = get_valids(raw_valids)
print ("\nvalid data")
print(tabulate(valids, headers="keys", tablefmt="grid"))

supplier_synopsis = supplier_summ(valids)
print("\nsupplier_summary")
print(tabulate(supplier_synopsis, headers="keys", tablefmt="grid"))

region_synopsis = region_summ(valids)
print("\nregion_summary")
print(tabulate(region_synopsis, headers="keys", tablefmt="grid"))