from django import forms
from .models import Writing
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User




class WritingCreateForm(forms.ModelForm):

	class Meta:
		model = Writing
		fields = [
			'title',
			'body',
			'category',
		]
