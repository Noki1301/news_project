from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muvaffaqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Sizning profilingiz bloklangan")
            else:
                return HttpResponse("Login yoki parol xato")
    else:
        form = UserLoginForm()
        context = {"form": form}
    return render(request, "registration/login.html", context=context)


def dashboard_view(request):
    user = request.user
    context = {"user": user}
    return render(request, "pages/user_profile.html", context=context)


def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html")
