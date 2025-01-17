from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            messages.success(request,("You have successful login.. "))
            return redirect ('home')
        # Return an 'invalid login' error message
        else:
            messages.success(request,("There Was An Error Login Try Again"))
            return redirect ('login')
    else:
        return render(request, 'authenticate/login.html', {})

#logout

def logout_user(request):
    logout(request)
    messages.success(request,("You Were Logged Out"))
    return redirect ('login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (" Registration Successful.."))
            return redirect ('home')
    
    else:
        form = UserCreationForm()
        
    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })