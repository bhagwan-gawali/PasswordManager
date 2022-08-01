from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):

	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = get_user_model()
		fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
		
class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')