from django.urls import path
from .views import SignUpView, SignInView, LogOutView


urlpatterns = [
    path("register", SignUpView.as_view(), name="signup_page"),
    path("", SignInView.as_view(), name="signin_page"),
    path("logout", LogOutView.as_view(), name="logout_page"),
]
