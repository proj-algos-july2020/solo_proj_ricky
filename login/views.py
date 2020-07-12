from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def registration(request):
    errors = User.objects.basic_validator(request.POST, 'registration')
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], phone_number=request.POST['phone_number'], password = pw_hash)

        return redirect('/registered')

def registered(request):
    return redirect('/')

def login(request):
    errors = User.objects.basic_validator(request.POST, 'login')
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect("/sports") #redirect to success route
        # return redirect('/')

def success(request):
    page_user = User.objects.get(id = request.session['userid'])
    context = {
        'page_user':page_user,
    }
    return render(request, 'success.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')
    
            

# Create your views here.
