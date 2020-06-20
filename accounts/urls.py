from django.conf.urls import url
from django.contrib.auth import views as auth_views
# Django 1.11 introduced login and logout view. We dont have to create classes
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'login/$',
        views.LoginView.as_view(template_name='accounts/login.html'),
            name = 'login'),
    url(r'logout/$',
            auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
]
