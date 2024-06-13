from django.contrib import auth
from django.shortcuts import redirect, render
from tutorial.forms import RegistationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
        else:
            print(form.errors)
            return redirect("register")

    else:
        form = RegistationForm()
        return render(request, "register.html", {"form": form})
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
        
        else:
            print(form.errors)
            return redirect("login")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    
def logout(request):
    auth.logout(request)
    return redirect("home")