from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import User
from . import forms
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    # WHen someone signe up, he will go to login page
    template_name = 'accounts/signup.html'

class LoginView(auth_views.LoginView):
    #fields = ('name', 'description')
    model = User
    form_class = LoginForm
