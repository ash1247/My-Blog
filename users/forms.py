from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #required = true
#class meta --> gives nested namespace for configurations and keeps the configuarations in one place
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2'] #the fields are showed in given order


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
			