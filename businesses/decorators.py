from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from inertia import render




#this is a custom decorator that prevents logged in users from accessing the  login or resgister endpoints
def allow_guest_only(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return render(request,'Index')
        else:
            return func(request,*args,**kwargs)
    return wrapper



#this is a custom decorator that prevents a user from hitting an endpoint unless they are logged in    
def only_logged_in_users(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return render(request,'Auth')
        else:    
            return func(request,*args,**kwargs)
    return wrapper
        
    