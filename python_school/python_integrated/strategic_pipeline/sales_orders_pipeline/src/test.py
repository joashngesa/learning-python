from tabulate import tabulate
from reader import read_file
from config import INPUT_PATH
from converter import convert_data
from sifter import split_invalids_valids
from sifter import duplicates_data
from transformer import transform_data
from transformer import summarize_supplier_category

if __name__=="__main__":

    raw = read_file(INPUT_PATH)
    print("raw_data\n")
    print(tabulate(raw, headers="keys", tablefmt="grid"))

    converted = convert_data(raw)
    print("\nconverted data")
    print(tabulate(converted, headers="keys", tablefmt="grid"))

    invalids, valids = split_invalids_valids(converted)
    print("\ninvalid data")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))

    print("\nvalid data")
    print(tabulate(valids, headers="keys", tablefmt="grid"))

    duplicates = duplicates_data(invalids)
    print("\nduplicates data")
    print(tabulate(duplicates, headers="keys", tablefmt="grid"))

    transformed = transform_data(valids)
    summary = summarize_supplier_category(transformed)
    print("\ntransformed")
    print(tabulate(summary, headers="keys", tablefmt="grid"))