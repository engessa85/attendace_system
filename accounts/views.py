from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin


User = get_user_model()


def is_admin(user):
    return user.is_authenticated and user.is_superuser


class SignUpView(UserPassesTestMixin, View):

    def test_func(self):
        return is_admin(self.request.user)
    
    def get(self, request):
        print(request.user)
        return render(request, "accounts/signup_page.html")
    
    def post(self, request, format=None):
        print("posting")
        data = self.request.POST
        name = data["name"]
        email = data["email"]
        password = data["password"]
        confirm_password = data["passwor2"]

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
            else:
                if len(password) < 6:
                    messages.error(request, "Password must be at least 6 characters")
                else:
                    print("here")
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    messages.success(request, "User is created successfully")
                    return redirect("signin_page")
        else:
            messages.error(request, "Passwords to be mathced")

        return render(request, "accounts/signup_page.html")
    

class SignInView(View):
    def get(self, request):
        return render(request, "accounts/signin_page.html")
    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        User = authenticate(request, email = email, password = password)
        print(User)
        if User is not None:
            login(request=request, user=User)
            
            if User.is_data:
                return redirect("managment_index")
            elif User.is_info:
                return redirect("MainInfoView")
            elif User.is_permit:
                return redirect("permissions_index")
            else:
                 messages.error(request, "Not Authorized !!!")
        else:
            messages.error(request, "Invalid email or password.")
        return render(request, "accounts/signin_page.html")


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("signin_page")
