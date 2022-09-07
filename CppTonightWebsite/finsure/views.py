from django.shortcuts import render, redirect
import hashlib
import csv

def check_password_aaf(pan, entered_password):
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    file = open('/Users/sahilamritkar/Sahil Codes/Hackathons/Qubit_24hr_Hackathon/FINSURE/CppTonightWebsite/finsure/AAF_Database.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    df={}
    for i in range(len(rows)):
        df[rows[i][0]]=rows[i]
    
    db_password=df[pan][1]

    if(hashed_password==db_password):
        return True
    return False

def check_password_xyz(pan, entered_password):
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    file = open('/Users/sahilamritkar/Sahil Codes/Hackathons/Qubit_24hr_Hackathon/FINSURE/CppTonightWebsite/finsure/XYZ_Database.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    df={}
    for i in range(len(rows)):
        df[rows[i][0]]=rows[i]
    
    db_password=df[pan][1]

    if(hashed_password==db_password):
        return True
    return False




######FUNCTIONS####
def finsure_login(request):
    result=0
    result=check_password_aaf(request.GET['your_PAN'], request.GET['your_password'])
    print(result)
    if result==True:
        return render(request, 'finsure_finances.html', {})
    else:
        pass
        #return to this page
    return render(request, 'finsure_login.html', {})

def finsure_finances(request):
    return render(request, 'finsure_finances.html', {})

def finsure_otp(request):
    return render(request, 'finsure_otp.html', {})

def xyz_login(request):
    result=0
    result=check_password_xyz(request.GET['your_PAN'], request.GET['your_password'])
    print(result)
    if result==True:
        return render(request, 'xyz_loan.html', {})
    else:
        pass
        #return to this page
    return render(request, 'xyz_login.html', {})

def xyz_loan(request):
    return render(request, 'xyz_loan.html', {})

def xyz_accepted(request):
    return render(request, 'xyz_accepted.html', {})

def xyz_rejected(request):
    return render(request, 'xyz_rejected.html', {})