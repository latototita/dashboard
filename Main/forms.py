from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone_no','image','country','district',"password1","password2")
        image= forms.ImageField(label='Profile Picture',required=True)
        district= forms.CharField(label='State/Location/District/Region',required=True)
        phone_no=forms.CharField(label='Used to Contact You',required=True)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class Join_Prime_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('prime',)
    prime= forms.BooleanField(label='Become a Prime User',required=True)

class Join_Advance_Prime_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('advance_prime',)
    advance_prime= forms.BooleanField(label='Become an Advance Prime User',required=True)
