from django.shortcuts import render 


def login(request):     
        context = {
            "title":"Login",
            "error" : True,
            "message": "invalid Username or Password"
        }

        return render(request,"auth/login.html",context=context)