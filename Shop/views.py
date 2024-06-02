import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from Shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Home(request):
    product=Products.objects.filter(trending=1)
    return render(request,'shop/index.html',{"product":product})
def Register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Has been Completed")
            return redirect("login")
    return render(request,'shop/register.html',{"form":form})
def LoginPage(request):
    name=request.POST.get('username')
    pwd=request.POST.get('password')
    user=authenticate(request,username=name,password=pwd)
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid UserName or Password")
                return redirect('login')
    return render(request,'shop/login.html')
def add_to_cart(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.loads(request.body.decode("utf-8"))
            return JsonResponse(request,{"status":"LoginToAddCart"},status=200),
        else:
            return JsonResponse(request,{"status":"Login To Add Cart"},status=200),
    else:
        return JsonResponse(request,{'status':'Invalid Access'},status=200)
def LogoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'LogOut Successfully')
        return redirect("/")
def Collections(request):
    category=Catagory.objects.filter(status="0")
    return render(request,'shop/collections.html',{'category':category})
def collectionsView(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        product=Products.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"product":product,"category_name":name})
    else:
        messages.warning(request,"No such Products Found")
        return redirect("Collections")
def productDetails(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            product=Products.objects.filter(name=pname,status=0).first()
            return render(request,'shop/products/productDetails.html',{"product":product})
        else:
            messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
        messages.warning(request,"No item is Found")
        return redirect("collections")
        