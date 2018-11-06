from django import forms
from .models import User
from writers import settings
from django.core.validators import ValidationError


class RegisterUserForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email',
			'gender',
			'location',
			'birth_date',
			'picture']

		help_texts = {
            'username': None,
        }

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password2 != password1:
			raise ValidationError("Passwords don't match")
		return password2
