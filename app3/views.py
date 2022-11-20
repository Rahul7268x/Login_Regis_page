from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        user=auth.authenticate(username=username1, password=password1)
        if user is None:
            return redirect('login')
        else:
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'login.html')
