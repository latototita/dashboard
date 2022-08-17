from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone_no','image','country','district','bank',"password1","password2")



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class Join_Prime_Form(UserChangeForm):

    class Meta:
        model = User
        fields = ('prime',)

class Join_Advance_Prime_Form(UserChangeForm):

    class Meta:
        model = User
        fields = ('advance_prime',)
