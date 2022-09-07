from django.shortcuts import render
import hashlib

def check_password():
    entered_password="Sahil"
    hashed_password=hashlib.md5(entered_password.encode()).hexdigest()
    database_password="dc4f69afa57999393ff0988bbdff1181" #use django to find 

    if(entered_password==database_password):
        return True
    return False

###
def finsure_login(request):
    print(request.GET)
    return render(request, 'finsure_login.html', {})