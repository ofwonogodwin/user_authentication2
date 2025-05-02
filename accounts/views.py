from django.shortcuts import render,redirect

# for register
from django.contrib import messages
from django.contrib.auth.models import User

# For login
from django.contrib.auth import authenticate, login

# For Log out
from django.contrib.auth import logout

# for dashboard
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request,"Passwords Dont Match")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already Taken.")
            return redirect('register')
        
        user = User.objects.create_user(username=username,pasword=password)
        user.save()
        messages.success(request,"Registration Success")
        return redirect('login')
    return render(request,'register.html')

# login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})



# logout
def logout_view(request):
    logout(request)
    return redirect('login')

# dashboard

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



