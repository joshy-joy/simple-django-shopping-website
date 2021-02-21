from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST.get('email'))
            if user.password == request.POST.get("password"):
                request.session["active_user"] = user.email
                return redirect('/')
            return render(request, "login.html", {'error': "Password mismatch"})
        except User.DoesNotExist:
            return render(request, "login.html", {'error': "User not exist"})
    return render(request, "login.html", {'error': False})


def signup(request):
    if request.method == 'POST':
        try:
            duplicate_user = User.objects.get(email = request.POST.get("email"))
            if duplicate_user:
                return render(request, "signup.html", {'error': "Email already exist. Please login"})
        except User.DoesNotExist:
            if request.POST.get("password") == request.POST.get("reenter-password"):
                user = User()
                user.first_name = request.POST.get("firstname")
                user.last_name = request.POST.get("lastname")
                user.email = request.POST.get("email")
                user.phone = request.POST.get("phone")
                user.password = request.POST.get("password")
                user.save()
                return redirect('/auth/login/')
            return render(request, "signup.html", {'error': "password not matching"})
    return render(request, "signup.html", {'error': False})

def logout(request):
    request.session["active_user"] = None
    return redirect("/auth/login/")
