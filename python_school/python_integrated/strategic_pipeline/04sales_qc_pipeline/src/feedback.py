#Pipeline completed successfully.

#Records processed: 20
#Valid records: 11
#Invalid records: 9

def output_report (raw,valids,invalids):
    
    print ("Pipeline completed successfully")
    print ("\nRecords processed: ",len(raw))
    print ("Valid records: ",len(valids))
    print ("Invalids records: ",len(invalids))