from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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


@login_required
def dashboard_view(request):
    user = request.user
    profile_info = Profile.objects.get(user=user)
    context = {"user": user, "profile_info": profile_info}
    return render(request, "pages/user_profile.html", context=context)


def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html")


def user_register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {"new_user": new_user}
            return render(request, "accounts/register_done.html", context=context)
    else:
        user_form = UserRegisterForm()
        context = {"user_form": user_form}
        return render(request, "accounts/register.html", context=context)


# class SignUpView(CreateView):
#     form_class = UserRegisterForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/register.html"


@login_required
def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("/")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, "accounts/edit_profile.html", context=context)


class EditUserView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, "accounts/edit_profile.html", context=context)

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("user_profile")
