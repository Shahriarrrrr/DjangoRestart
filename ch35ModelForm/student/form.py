from django import forms
from .models import Profile



class Registration(forms.ModelForm):
    confirm_password = forms.CharField() # i dont want this to besaved in Database thats why declared here
    class Meta:
        model = Profile
        fields = ['name',  'email', 'password', 'phone']
        labels = {'name': 'Enter name', 'email' : "Enter email"}
        error_messages = {
            'email': {'required': "Email is required"}
        }
        widgets = {
            'password': forms.PasswordInput(attrs=
                                            {'class': "pwdclass"}),
                                            'name': forms.TextInput(attrs= {'class': 'myclass',
                                                                    'placeholder': 'Type Name Here'})

        }