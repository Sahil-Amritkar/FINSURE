import email
from http import server
import math
import random
import smtplib
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib
import csv

def check_password_aaf(pan, entered_password):
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    file = open('../CppTonightWebsite/finsure/AAF_database.csv')
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
    file = open('../CppTonightWebsite/finsure/XYZ_database.csv')
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


def otp_generate(request):
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    OTP = str(4578)
    return OTP


def send_email(request):
    smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<gmail id>', '<gmail password>')
    msg = '<p>Your OTP is <strong>'+o+'</strong></p>'
    server.sendmail('<gmail id>', email, msg)
    o=0
    server.quit()
    return HttpResponse(o)


def send_otp(request):
    email = request.GET.get("email")
    o = otp_generate()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    print(send_mail('OTP', htmlgen, '<gmail id>',
          [email], fail_silently=False))
    print(o)
    return HttpResponse(o)




######FUNCTIONS####
def finsure_login(request):
    result=0
    result = check_password_aaf(request.POST.get(
        'your_PAN', 'VITCC0001A'), request.POST.get('your_password', 'Sahil'))
    print(result)
    if result==True:
        return render(request, 'finsure_finances.html', {})
    else:
        pass
        #return redirect('finsure_login')
    #return to this page
    return render(request, 'finsure_login.html', {})


def finsure_finances(request):
    return render(request, 'finsure_finances.html', {})


def finsure_otp(request):
    print(request.GET)
    return render(request, 'finsure_ticktick.html', {})

def finsure_ticktick(request):
    return render(request, 'xyz_approved.html')


def xyz_login(request):
    result=0
    result = check_password_aaf(request.POST.get(
        'your_PAN', 'VITCC0001A'), request.POST.get('your_password', 'Sahil'))
    print(result)
    if result==True:
        return render(request, 'xyz_loan.html', {})
    else:
        pass
    #return to this page
    return render(request, 'xyz_login.html', {})


def xyz_loan(request):
    print("loan page")
    print(request.GET)
    return render(request, 'finsure_otp.html', {})


def xyz_accepted(request):
    return render(request, 'finsure_login.html', {})


def xyz_rejected(request):
    return render(request, 'xyz_rejected.html', {})



