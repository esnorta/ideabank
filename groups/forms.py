from django import forms
from groups.models import Group


class GroupForm(forms.ModelForm):
    model = Group
    fields = ['name', 'description']

    widgets = {
        'name': forms.TextInput(attrs = {'class': 'textinputclass'}),
        'description': forms.TextInput(attrs = {'class': 'textinputclass'}),
    }
