from django.contrib.auth import  get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

        labels = {
            'Username':'',
            'password':'',
        }


    def __init__(self,*args,**kwargs):
        # If I want labels on the field pf the form
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

  #  username = forms.EmailField(widget=forms.TextInput(
  #      attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
  #  password = forms.CharField(widget=forms.PasswordInput(
  #      attrs={
  #          'class': 'form-control',
  #          'placeholder': '',
  #          'id': 'hi',
  #      }
  #  ))

    class Meta():
        model = get_user_model()
        fields = ('username', 'password')
        widgets = {
                'username': forms.TextInput(attrs = {'class': 'textinputclass',
                        'type':'text', 'placeholder' : 'Название новой супер идеи'}),
                'password': forms.TextInput(attrs = {'class': 'textinputclass',
                        'placeholder': False}),
            }

        labels = {
            'Username':'',
            'Password':'',
        }


