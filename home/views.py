from django.shortcuts import render,redirect, get_object_or_404
from .forms import basic_info_form, loginForm, signUp, forgotPasswordForm
from .models import Users_info, Dog, Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == "POST":
        form = basic_info_form(request.POST)
        if form.is_valid():
            user = Users_info(
                Uname = form.cleaned_data['name'],
                umail = form.cleaned_data['email']
            )
            user.save()
            dog = Dog(
                dogName = form.cleaned_data['dogname'],
                dogBreed = form.cleaned_data['dogbreed'] 
            )
            
            dog.save()
            return redirect('home')
    else:
        form = basic_info_form()
    return render(request,'index.html', {"form" : form})

def loginUser(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            print(username)
            password = request.POST.get('password')

        # Authenticate the user
            user = authenticate(request, username=username, password=password)
            request.session.set_expiry(60)
            
            
            if user is not None:
                user.is_active = True
            # User is authenticated, log them in
                
                login(request, user)
                return redirect('profile')
            else:
            # Invalid credentials, show error message
                error_message = 'Invalid user credentials'
                print(error_message)
                return render(request, 'login.html', {'error_message': error_message})

    else:
        form = loginForm()
    return render(request, 'login.html' , {'form':form}) 
    

def signup(request):
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password'] 
            email_name, domain_part = email.strip().rsplit("@", 1)

            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.email_name = email_name
            user.domain_part = domain_part
            user.save()

           
            return redirect('home')
            
    else:
        form = signUp()
    return render(request, 'signUp.html',{"form":form})

@login_required
def profile(request):
    user = request.user
    username = user.username
    email = user.email

    return render(request, 'profile.html', {'username': username, 'email' : email})

def logout_user(request):
    if request.method == 'POST':
        # Clear session data
        request.session.flush()
        return redirect('home')
    elif request.method == 'GET':
        return render(request, "login.html")
    else:
        return HttpResponseNotAllowed(['POST','GET'])
    
def forgot_password(request):
    form = forgotPasswordForm()
    if request.method == "POST":
        form = forgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['mail']
            confirmedMail = emailCheck(email)
            if confirmedMail:
                subject = "change Password"
                message = "not now but soon"
                fromEmail = "rajat.tiggit@gmail.com"
                recipient_list = [email]
                send_mail(subject, message, fromEmail, recipient_list)
                return render(request, 'example.html',{"message":"found"})
            else:
                return render(request, 'example.html',{"message":"notfound email not found"})
            return redirect('home')
    else:
        form = forgotPasswordForm()
    return render(request, 'forgotPassword.html', {'form':form})

def emailCheck(email):
    return User.objects.filter(email=email).exists()

    




  
