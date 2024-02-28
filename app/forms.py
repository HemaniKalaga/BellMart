from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.
    
   

class Profile(forms.ModelForm):
    Re_enter_email=
    Re_enter_password=
    Mobile=
    address=

