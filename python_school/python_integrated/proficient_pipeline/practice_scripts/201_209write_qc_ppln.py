                            #CUSTOMER SIGN UP QUALITY PIPELINE
#🗺️Create a pipeline that:
#→ convert / clean ▶️
#→ validate records ▶️
#→ split valid and invalid ▶️▶️
#→ detect duplicate emails ▶️
#→ transform valid records▶️
#→ produce metrics ▶️
#→ produce quality report ▶️
#write output to result folder ✅
#create pipeline that exec_qc_pipeline ✅
#▶️ represents successfully tested functions
# ✅ represents written codes

import os
import csv
from tabulate import tabulate

raw_signups = [
    {"signup_id": "S001", "name": "Amina", "email": "amina@mail.com", "age": "25", "plan": "premium"},
    {"signup_id": "S002", "name": "Brian", "email": "brian@mail.com", "age": "17", "plan": "basic"},
    {"signup_id": "S003", "name": "", "email": "claire@mail.com", "age": "31", "plan": "premium"},
    {"signup_id": "S004", "name": "David", "email": "amina@mail.com", "age": "28", "plan": "basic"},
    {"signup_id": "S005", "name": "Eve", "email": "eve@mail.com", "age": "abc", "plan": "premium"},
    {"signup_id": "S006", "name": "Frank", "email": "frank@mail.com", "age": "44", "plan": "gold"},
    {"signup_id": "S007", "name": "Grace", "email": "grace@mail.com", "age": "36", "plan": "basic"},
]
                    #print(tabulate(raw_signups, headers="keys", tablefmt="grid"))

def convert_raw(file_name):
    converted_tbl = []
    for mail in file_name:
        new = mail.copy()
        try:
            new["age"] = int(new["age"]) if new["age"] != "" else None
            #checks if the column age value is null and converts to integer from string
        except ValueError:
            new["age"] = None

        converted_tbl.append(new)

    return converted_tbl

                    #converted = convert_raw(raw_signups)    
print("[INFO] conversion complete")
                    #print(tabulate(converted,headers="keys", tablefmt="grid"))


#validation rules
#signup_id is a non-empty string
#name is a non-empty string
#email is a non-empty string
#age is an integer
#age >= 18
#plan is either "basic" or "premium"
#email is not duplicated

#business rule; do not allow duplicate email

input_columns = ["signup_id","name","email","age","plan"]

def validate_tbl(mail):
    for column in input_columns:
        if column not in mail:
            return False, f"the column {column} not found" 
        
    signup_id = mail.get("signup_id")  
    name = mail.get("name")
    email = mail.get("email")
    age = mail.get("age")
    plan = mail.get("plan")
    allowed_plan = ["basic","premium"]
    if not isinstance (signup_id,str) or signup_id.strip() == "":
        return False,"the signup_id should be non_empty string"
    if not isinstance (name,str) or name.strip() =="":
        return False, "the name should be a non_empty string"
    if not isinstance (email,str) or email.strip() =="":
        return False, "the email should be a non_empty string"
    if not isinstance (age,int):
        return False, "the age should be integer" 
    if age < 18:
        return False, "age should be above 18"
    if plan not in allowed_plan:
        return False, "plan should be either basic or premium"
    
    return True, "valid"
 
def get_invalids_valids(converted):
    invalids = []
    valids = []
    seen_emails = set()

    for mail in converted:
        is_valid, reason = validate_tbl(mail)

        if not is_valid:
            invalid_data = mail.copy()
            invalid_data["error reasons"] = reason
            invalids.append(invalid_data)
            continue

        email = mail.get("email")

        if email in seen_emails:
            invalid_data = mail.copy()
            invalid_data["error reasons"] = "duplicate email"
            invalids.append(invalid_data)
            continue

        seen_emails.add(email)
        valids.append(mail)

    return invalids,valids

                    #invalids, valids = get_invalids_valids(converted)
                    #print(tabulate(invalids,headers="keys", tablefmt="grid"))
                    #print(tabulate(valids,headers="keys", tablefmt="grid"))

#age group rules:
#18–29 → young_adult
#30–44 → adult
#45+   → mature_adult
def group_age(mail):
    age = mail.get("age")

    if 18 <= age <= 29:
        return "young adult"
    elif 30 <= age <= 44:
        return "adult"
    elif age >= 45:
        return "mature adult" 
    else:
        return None
    

#transformed data:
#signup_id
#name
#email
#plan
#age_group
def transform_data(valids):
    return [
        {
            "signup_id": mail.get("signup_id"),
            "name": mail.get("name"),
            "email": mail.get("email"),
            "plan": mail.get("plan"),
            "age_group": group_age(mail)
        }
        for mail in valids
    ]

                    #transformed = transform_data(valids)
                    #print(tabulate(transformed,headers="keys", tablefmt="grid"))


#produce metrics:
#"total_valid_signups": ...
#basic_plan_count": ...,
#premium_plan_count": ...,
#young_adult_count": ...,
#"adult_count": ...,
#"mature_adult_count": ...

def premium_plan_count(transformed):
    return sum([1 for mail in transformed if mail.get("plan") == "premium"])

                    #ppc = premium_plan_count(transformed)
                    #print(ppc)

def young_adult_count(transformed):
    return sum([1 for mail in transformed if mail.get("age_group") == "young adult"])

                    #yac = young_adult_count(transformed)
                    #print(yac)

def adult_count(transformed):
    adult_tot = 0
    for mail in transformed:
        if mail.get("age_group") == "adult":
            adult_tot += 1
    
    return adult_tot

                   # ad = adult_count(transformed)
                   # print(ad)

def mature_adult_count(transformed):
    mature_ad_cnt = 0
    for mail in transformed:
        if mail.get("age_group") == "mature adult":
            mature_ad_cnt += 1

    return mature_ad_cnt

                    #mac = mature_adult_count(transformed)


def data_metrics(transformed):
    basic_plan_cnt = 0
    for mail in transformed:
        if mail.get("plan") == "basic":
            basic_plan_cnt += 1

    return [
    {
        "total_valid_signups": len(transformed),
        "basic_plan_count": basic_plan_cnt,
        "premium_plan_count": premium_plan_count(transformed),
        "young_adult_count": young_adult_count(transformed),
        "adult_count": adult_count(transformed),
        "mature_adult_count": mature_adult_count(transformed)
    }
    ]

                    #metrics = data_metrics(transformed)
                    #print(tabulate(metrics, headers="keys", tablefmt="grid"))


#quality report:
#total_records": ...,
#valid_records": ...,
#invalid_records": ...,
#valid_percentage": ...,
#invalid_percentage": ...,
#error_summary": ...
def quality_report(converted,invalids,valids):
    tot_records = len(converted)
    valid_records = len(valids)
    invalid_records = len(invalids)

    if tot_records== 0:
        valid_pcnt = 0
        invalid_pcnt = 0

    else:
        valid_pcnt = round((valid_records/tot_records) * 100,2)
        invalid_pcnt = round((invalid_records/tot_records) * 100,2)

    return  [
    {
        "total_records": tot_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "valid_percentage": valid_pcnt,
        "invalid_percentage": invalid_pcnt 
    }
    ]

                    #qc_report = quality_report(converted,invalids,valids)
                    #print(tabulate(qc_report, headers="keys", tablefmt="grid"))


#error summary function that counts per error reason
def error_summary(invalids):
    errors_list = {}

    for mail in invalids:
        cases = mail.get("error reasons")
        if cases not in errors_list:
            errors_list[cases] = 1
        else:
            errors_list[cases] += 1

   # error_tbl = []
    #for reason, count in errors_list.items():
    #    error_tbl.append({
     #       "error reason": reason,
      #      "count": count
       # })

    error_tbl = [{"error reasons": reasons, "count": count}
                 for reasons,count in errors_list.items()]
    
    return error_tbl

def show_output(invalids,valids,transformed,metrics,qc_report):
    print("\ninvalid tables")
    print(tabulate(invalids,headers="keys", tablefmt="grid"))
    print("\nvalid tables")
    print(tabulate(valids,headers="keys", tablefmt="grid"))
    print("\n transformed table")
    print(tabulate(transformed,headers="keys", tablefmt="grid"))
    print("\noutput metrics")
    print(tabulate(metrics,headers="keys", tablefmt="grid"))
    print("\nerror reports")
    print(tabulate(qc_report,headers="keys", tablefmt="grid"))
    print("\nqc_report")
    print(tabulate(qc_report,headers="keys", tablefmt="grid"))



def write_ppln_output(output_path,data,output_delimiter,output_columns):
    folder_path = os.path.dirname(output_path)

    if folder_path:
        os.makedirs (folder_path, exist_ok=True)


    with open (output_path, "w", newline="") as file:
        writer = csv.DictWriter (file,delimiter=output_delimiter,fieldnames=output_columns,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

invalids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/customer_signup_ppln/client_signup_invalids.csv"
valids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/customer_signup_ppln/client_signups_valids.csv"
trfmd_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/customer_signup_ppln/client_signups_processed.csv"
metrics_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/customer_signup_ppln/output_metrics.csv"
qc_summary_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/customer_signup_ppln/qc_summary.csv"


invalid_columns = ["signup_id","name","email","age","plan","error reasons"]
valids_columns = ["signup_id","name","email","age","plan"]
trfmd_columns = ["signup_id","name","email","plan","age_group"]
metrics_columns = ["total_valid_signups","basic_plan_count","premium_plan_count","young_adult_count","adult_count","mature_adult_count"]
qc_columns = ["total_records","valid_records","invalid_records","valid_percentage","invalid_percentage"]

              
def exec_qc_write_csv_pipeline(file_name,output_delimiter):
    converted = convert_raw(file_name) 
    if converted is None:
        return {
            "status": "failed",
            "reason": "conversion failed"
        }
    
    invalids, valids = get_invalids_valids(converted)
    transformed = transform_data(valids)
    metrics = data_metrics(transformed)
    qc_report = quality_report(converted,invalids,valids)
    show_output(invalids,valids,transformed,metrics,qc_report)
    write_ppln_output(invalids_path,invalids,output_delimiter,invalid_columns)
    write_ppln_output(valids_path,valids,output_delimiter,valids_columns)
    write_ppln_output(trfmd_path,transformed,output_delimiter,trfmd_columns)
    write_ppln_output(metrics_path,metrics,output_delimiter,metrics_columns)
    write_ppln_output(qc_summary_path,qc_report,output_delimiter,qc_columns)

    return {
        "status": "success",
        "pipeline metrics": metrics
    }

exec_qc_write_csv_pipeline(raw_signups,"|")
