from tabulate import tabulate

#OUTPUT 
#total raw rows
#valid records
#invalid records
#duplicate records
#summary table

def print_pipeline_output(raw,invalids,valids,duplicates,transformed,summary):
    print("total raw rows: ",len(raw))
    print("\ninvalid data")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nvalid data")
    print(tabulate(valids, headers="keys", tablefmt="grid"))
    print("\nduplicates data")
    print(tabulate(duplicates, headers="keys", tablefmt="grid"))
    print("\ntransformed table")
    print(tabulate(transformed, headers="keys", tablefmt="grid"))
    print("\nsummary table")
    print(tabulate(summary, headers="keys", tablefmt="grid"))