from django.shortcuts import render, redirect
import hashlib
import csv

def check_password(pan, entered_password):
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    #database_password="dc4f69afa57999393ff0988bbdff1181" #use django to find 
    file = open('/Users/sahilamritkar/Sahil Codes/Hackathons/Qubit_24hr_Hackathon/FINSURE/CppTonightWebsite/finsure/AAF_Database.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    df={}
    for i in range(len(rows)):
        df[rows[i][0]]=rows[i]
        # for j in range(len(header)):
        #     df[rows[i][0][header[j]]]=rows[i][j]
    

    db_password=df[pan][1]

    if(hashed_password==db_password):
        return True
        #finsure_finances(1)
    return False
    #finsure_login(1)

###
def finsure_login(request):
    result=0
    result=check_password(request.GET['your_PAN'], request.GET['your_password'])
    print(result)
    if result==True:
        pass
    else:
        pass
        #return to this page
    return render(request, 'finsure_login.html', {})

def finsure_finances(request):
    return render(request, 'finsure_finances.html', {})

def finsure_otp(request):
    return render(request, 'finsure_otp.html', {})