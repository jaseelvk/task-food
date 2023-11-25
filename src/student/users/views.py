from django.shortcuts import render 
from django.contrib.auth import authenticate , login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request,user)
                url=f'/{user.pk}'
                return HttpResponseRedirect(url)

            
        context = {
            "title":"Login",
            "error" : True,
            "message": "invalid Username or Password"
        }
        return render(request,"auth/login.html",context=context) 
    else:
        context = {
            "title":"Login"
        }
        return render(request,"auth/login.html",context=context)