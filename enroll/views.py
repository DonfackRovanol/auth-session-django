from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# signup views.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Create Successfully!!')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})

#login views
def user_login(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponsePermanentRedirect('/profile/')
        else:
            form = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': form})
    else:
        return HttpResponsePermanentRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponsePermanentRedirect('/login/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect('/login/')