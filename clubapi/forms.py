from django import forms

from . import models

class OwnerForm(forms.ModelForm):
	class Meta:
		models = models.OwnerForm
		filed = '__all__'