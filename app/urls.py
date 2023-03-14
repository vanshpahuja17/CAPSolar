from django.urls import path
from .views import *

urlpatterns = [
    path("register/", Register, name="register"),
    path("", Login, name="login"),
    path("logout/", Logout, name="logout"),

    path("otp-verification/", VerifyOTPPage, name="verifyotppage"),
    path("forgot-password-email/", FpEmailPage, name="fpemailpage"),
    path("forgot-password-otp/", FpOTPPage, name="fpotppage"),
    path("forgot-password-reset/", FpPasswordPage, name="fppasswordpage"),

    path("threshold_sample/", Threshold , name="threshold_sample"),

    path("verify-otp/", VerifyOTP, name="verify-otp"),
    path("fp-email/", FpEmail, name="fp-email"),
    path("fp-otp/", FpOTP, name="fp-otp"),
    path("fp-password/", FpPassword, name="fp-password"),

    path("dashboard/", Dashboard, name="dashboard"),
    path("notifications/", notifications, name="notifications")
]