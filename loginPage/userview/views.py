from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginform(request):
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user= authenticate(request, username=username, password= password)
       if user is not None:
           login(request, user)
           messages.success(request, 'You been Logged in')
           return HttpResponse('logged in')
       else:
           return HttpResponse('Failed.')
   else:
        return render(request, 'login.html')

def logout(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('loginform')