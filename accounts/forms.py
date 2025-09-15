from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class CustomAuthForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Login yoki parol noto‘g‘ri. Iltimos, qayta tekshirib kiriting.",
        "inactive": "Hisobingiz faol emas.",
    }


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Parol", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_2 = forms.CharField(
        label="Parolni takrorlang",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password_2"]:
            raise forms.ValidationError("Kiritgan parollaringiz bir biriga mos emas!")
        return data["password_2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "date_of_birth"]
        widgets = {
            "photo": forms.FileInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control"}),
        }
