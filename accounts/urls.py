from django.urls import path
from .views import user_login
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import user_login, dashboard_view, user_register, edit_user, EditUserView
from .forms import CustomAuthForm

ap_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(authentication_form=CustomAuthForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", dashboard_view, name="user_profile"),
    # path("profile/edit/", edit_user, name="user_edit"),
    path("profile/edit/", EditUserView.as_view(), name="user_edit"),
    # path("signup/", SignUpView.as_view(), name="user_register"),
    path("signup/", user_register, name="user_register"),
]
