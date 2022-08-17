from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone_no','image','country','district','bank',)


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
