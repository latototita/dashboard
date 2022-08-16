from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
	class Meta:
		models=Payment
		fields=("amount","email")