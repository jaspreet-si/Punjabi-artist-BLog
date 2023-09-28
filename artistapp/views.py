from django.shortcuts import render,redirect
from .models import *
from  .forms import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    show=artist.objects.all()
    return render(request,'home.html',{"show":show})
@login_required(login_url='Login')

def readmore(request,id):
    data =artist.objects.get(id=id)
   
    return render(request,'readmore.html',{"data":data})

def contact(request):
    if request.method=='GET': # jekar method get hai mtlb user ton data laina hai tan eh page show kraao
        form=contactform()
        return render(request,'contact.html',{"form":form})
    else:
        form=contactform(request.POST)  #nhi te form nu post krdo
        if form.is_valid():  
            form.save()
        return redirect(homepage)

def Login(request):
    if request.method=="GET":

       return render(request,'login.html')
    else:
        username=request.POST['userName']
        email=request.POST['Email']
        password=request.POST['Password']

        user=auth.authenticate(username=username,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(homepage)

        else:
            messages.warning(request,'invalid username or password ')
            return redirect('Login')

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        userName=request.POST['userName']
        email=request.POST['Email']
        Pass1=request.POST['Password']
        Pass2=request.POST['ConfirmPass']

        if Pass1==Pass2:
                # by default there is name given by model username,email
            if User.objects.filter(username=userName).exists():
                messages.warning(request,'Username already exists')
                return redirect('signup')
            
            elif User.objects.filter(email=email).exists():# suggests that it is trying to filter data from a database or a collection based on the "email" field. The variable email presumably holds the email address you want to use for filtering
                messages.warning(request,'Email already exists')
                return redirect('signup')
            
            #
            
            else:
                User.objects.create_user(username=userName,email=email,password=Pass1)
                messages.success(request,'account has been created')
                return redirect('Login')
        else:
            messages.warning(request,'password does not match')
            return redirect('signup')


            
def logout(request):
    auth.logout(request)
    return redirect('Login')

def find(request):
    if request.method=="POST":
        search=request.POST['search']
        if artist.objects.filter(Singer_name__contains=search).exists():
            data=artist.objects.filter(Singer_name__contains=search)
            return render(request,'home.html',{"data":data})
        else:
            messages.warning(request,'invalid search')
            return redirect(homepage)
    else:
        return redirect('homepage')
    


