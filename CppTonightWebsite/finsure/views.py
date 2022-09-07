from django.shortcuts import render

def finsure_login(request):
    print(request.GET['your_PAN'])
    return render(request, 'finsure_login.html', {})