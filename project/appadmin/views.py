from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

from .models import admindetails

# Create your views here.
def homefunction(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    # return render(request,'home.html')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('superhome')
            else:
                return redirect('home')
        else:
            messages.error(request,"invalid Username or Password")
            return redirect('home')
    return render(request,'home.html')

def superhome(request):
    admins=admindetails.objects.all()

    return render(request,'superadmin_home.html',{'admins':admins})
def createadmin(request):
    if request.method=='POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        admins=admindetails.objects.create(name=name,username=username,password=password)
        admins.save()
        print(admins)
        return redirect('superhome')
    return render(request,'createadmin.html')
def logoutfunction(request):
    logout(request)
    # return render(request,'home.html')
    return redirect('home')
def deletefunction(request,id):
    admins=admindetails.objects.get(id=id)
    admins.delete()
    return redirect('superhome')
def editfunction(request,id):
    edit=admindetails.objects.get(id=id)
    if request.method=='POST':
        if edit:
            edit.name=request.POST.get('name')
            edit.username=request.POST.get('username')
            edit.password=request.POST.get('password')
        edit.save()
        return redirect('superhome')
    return render(request,'editadmin.html',{'edit':edit})
