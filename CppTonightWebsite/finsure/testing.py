import hashlib
import csv


def check_password_xyz(pan, entered_password):
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    file = open('/Users/sahilamritkar/Sahil Codes/Hackathons/Qubit_24hr_Hackathon/FINSURE/CppTonightWebsite/finsure/XYZ_database.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    df={}
    for i in range(len(rows)):
        df[rows[i][0]]=rows[i]
    print(df)
    
    db_password=df[pan][1]
    print(hashed_password, db_password)

    if(hashed_password==db_password):
        return True
    return False


print(check_password_xyz("VITCC0001A",'Sahil'))