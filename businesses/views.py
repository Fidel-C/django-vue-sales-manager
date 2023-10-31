from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from inertia import render, share
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_GET, require_POST
from businesses.decorators import allow_guest_only, only_logged_in_users
from businesses.forms import LoginForm, SaleForm, StoreForm
from .models import Store

# Create your views here.


# this is to provide shared data as prop to every component
def inertia_share(get_response):
    def middleware(request):
        share(request, user=lambda: request.user)
        return get_response(request)

    return middleware


@only_logged_in_users
def logout_view(request):
    logout(request)
    return redirect("/")


@only_logged_in_users
def index(request):
    stores=request.user.store_set.all()
    print(stores)
    return render(request, "Index", {"user": request.user,'stores':stores})


@allow_guest_only
def auth_page(request):
    return render(request, "Auth")


@allow_guest_only
@require_POST
def register_view(request):
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(data="Ok")
    else:
        errors = form.errors.as_json()
        return JsonResponse(data=errors, status=422, safe=False)


@allow_guest_only
@require_POST
def login_view(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")
    else:
        print(form.errors)
        errors = form.errors.as_json()
        return JsonResponse(data=errors, status=422, safe=False)


@only_logged_in_users
@require_POST
def create_store(request):
    form = StoreForm(data=request.POST)
    if form.is_valid():
        form.save(request.user)
        return JsonResponse(data={})
    else:
        errors=form.errors.as_json()
        return JsonResponse(data={'errors':errors},status=422,safe=False)
        


# @only_logged_in_users
# @require_POST
# def create_sale(request):
#     form = SaleForm(data=request.POST)
#     store=Store.objects.get(id=request.POST.get('store'))
#     if form.is_valid():
        
#         Sale.objects.create()

#     form.save(request.user)
#     return JsonResponse(data={})
# else:
#     errors=form.errors.as_json()
#     return JsonResponse(data={'errors':errors},status=422,safe=False)

    
        
