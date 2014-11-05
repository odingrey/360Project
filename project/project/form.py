from django import forms            
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      
from models import UserProfile

import hashlib
import models

class UserRegistrationForm(UserCreationForm):
	username = forms.EmailField(required = True)
	password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')        

	def clean_email(self):
		email = self.cleaned_data['username']
		try:
			user = User.objects.get(email=email)
			raise forms.ValidationError("This email address already exists. Did you forget your password?")
		except User.DoesNotExist:
			return email

	def save(self,commit = True):   
		user = super(UserRegistrationForm, self).save(commit = False)
		user.username = self.cleaned_data['username']
		user.set_password(self.cleaned_data['password1'])
		user.email = user.username

		if commit:
			user.save()

		return user


class UserProfile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)



class UploadFileForm(forms.Form):
	name = forms.CharField(max_length=50)
	file = forms.FileField()
