from django.contrib.auth import  get_user_model
from django.contrib.auth.forms import UserCreationForm

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

