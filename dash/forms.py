from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

# class PatientForm(forms.Form):
#     subject = forms.CharField(max_length=100)