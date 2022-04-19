from django.shortcuts import render, redirect
from users.forms import signupForm
from django.contrib.auth import logout as django_logout, \
                                login as django_login,\
                                authenticate
from django.http import HttpResponse

# Create your views here.

def logout(request):
    django_logout(request)
    return redirect('main')

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return redirect('main')
    else:
        form = signupForm()

    return render(request, 'users/signup.html', {'form':form})