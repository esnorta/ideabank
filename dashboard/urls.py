from django.conf.urls import url
# Django 1.11 introduced login and logout view. We dont have to create classes
from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    url(r'dashboard/$', views.DashView, name='dashboard'),
]
